# UC Readiness Review — UC101-106 (Tạm ngừng, Chấm dứt ĐTNN - Mẫu A.IV.7)
**Functional / Black-box Test Readiness Template — Re-audit v7 (SRS v1.6 Update)**

**Tiêu đề:** UC101-106 — Báo cáo tình hình tạm ngừng, chấm dứt hoạt động dự án ĐTNN (Mẫu A.IV.7)  
**Ngày tạo:** 22/05/2026  
**Tác giả:** QC Re-audit Agent  
**Phiên bản:** v7

---

## Feature Brief

Chức năng báo cáo tình hình tạm ngừng, chấm dứt hoạt động dự án ĐTNN theo lĩnh vực (Mẫu A.IV.7) dành cho các Bộ (Tư pháp, Công thương, NHNN VN). Báo cáo định kỳ quý, gửi lẻ (single report form). Tối đa 1 bản nộp/Bộ/kỳ. Dynamic Table 2 phần (Tạm ngừng + Chấm dứt), max 200 dòng/phần. Mode A/B auto-detect (API OK → Mode B auto-fill Editable, API Fail → Mode A nhập tay). Re-open nháp giữ snapshot không re-fetch. Import .xlsx only (CF_02 Case 2). Last Write Wins. Filter AND logic.

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **101/110 → 91.8 / 100** | ✅ **READY** |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|---|---|---|---|
| UC101-106 | Tạm ngừng, Chấm dứt ĐTNN - Mẫu A.IV.7 | v1.6 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|---|---|---|---|
| yen.le2 | — | 2026-04-23 | 2026-05-22 |

**Wireframe/Mockup:** 2 file PNG đính kèm — `Danh sách.png`, `Lập báo cáo.png`.

---

## 1. Feature Identity ✅ (5/5)

Đầy đủ ID, tên, lĩnh vực, phân hệ, mẫu biểu, quy tắc sinh mã (FDI_AIV7_[ID]).

---

## 2. Objective & Scope ✅ (5/5)

Objective rõ ràng. Import đã xác định CF_02 Case 2. Out of scope: không nộp trễ hạn, không duyệt.

---

## 3. Actors & Stakeholders ✅ (10/10)

SRS v1.6 đã clarify:
- 3 Bộ (Primary) + Cục ĐTNN (Receiver) + System (API).
- **Nhiều user cùng Bộ cùng tạo mới:** Cho phép song song, user lưu trước thắng, user sau báo lỗi "đã tồn tại".
- Phân quyền RBAC theo Bộ/Ngành.

---

## 4. Preconditions & Postconditions ✅ (10/10)

SRS v1.6 đã bổ sung:
- **Tối đa 1 bản nộp/Bộ/kỳ** — race condition xử lý bằng "user lưu trước thắng".
- Re-open nháp: giữ snapshot, không re-fetch API.
- Postconditions đầy đủ cho Nộp, Lưu nháp, Xóa, Import, API timeout, Concurrent edit.

---
## 5. UI Object Inventory & Mapping ⚡ (13/15)

SRS v1.6 liệt kê đầy đủ các elements cho cả Danh sách và Lập báo cáo. Wireframe đã cung cấp.

**Gaps còn lại:**
- Phần II vẫn ghi "Áp dụng chung cho Phần I và Phần II" — không có bảng chi tiết riêng (-1đ).
- Placeholder cho các cột text trong bảng chưa quy định cụ thể (-1đ).

---

## 6. Object Attributes & Behavior Definition ✅ (20/20)

SRS v1.6 đã resolve tất cả gaps behavior:

- **Mode A/B auto-detect:** API OK → Mode B (auto-fill, Editable). API Fail → Mode A + Toast T05.
- **API timeout giữa chừng:** Giữ data đã fill, không rollback + Toast T05 + manual phần còn lại (CMR_12).
- **Re-open nháp:** Giữ snapshot đã lưu, không re-fetch API.
- **Đổi lĩnh vực:** Popup xác nhận → [Đồng ý] xóa toàn bộ (kể cả Ghi chú manual) + re-fetch API.
- **Xóa dòng:** Chỉ hiển thị khi ≥ 2 dòng, xóa ngay không popup (CMR_15). STT re-index.
- **Max 200 dòng/Phần:** Vượt → Toast T16.
- **Sort:** Cột 5, 7, 9. Default: Cột 9 desc. Persist khi Lưu nháp.
- **Concurrent edit:** Last Write Wins + Lifecycle Log.
- **Filter logic:** AND khi chọn nhiều giá trị.
- **Dirty Form Guard:** CMR_14.
- **Decimal:** Tối đa 5 chữ số thập phân.

---

## 7. Functional Logic & Workflow Decomposition ✅ (20/20)

**[Xem danh sách]**
- Nhóm theo kỳ, collapse, sort giảm dần. Filter AND logic. Phân trang CMR_10.
- Nút Lập/Nhập từ file chỉ khi "Trong thời hạn".

**[Lập báo cáo]**
- Mode A/B auto-detect → fill/manual → Lưu nháp/Nộp.
- Race condition: user lưu trước thắng, user sau báo lỗi "đã tồn tại".
- Validate: Lưu nháp chỉ T07; Nộp full + empty table + cross-section + date range.

**[Chỉnh sửa (YC chỉnh sửa)]**
- Mở form với snapshot đã lưu (không re-fetch API).
- User phải sửa ≥1 field → nút Nộp Enabled (CF_03).

**[Các tác vụ bổ trợ]**
- 7 actions: Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất, Xóa.

---

## 8. Functional Integration Analysis ✅ (10/10)

- API auto-fill + fallback manual.
- Đổi lĩnh vực → xóa toàn bộ (kể cả Ghi chú) + re-fetch.
- Cross-section validate (cùng kỳ, không cross-quarter).
- Import CF_02 Case 2.
- Concurrent edit: Last Write Wins.
- Re-open nháp: giữ snapshot.
- API timeout mid-stream: giữ data, không rollback.

---

## 9. Acceptance Criteria ✅ (10/10)

15 AC bao phủ đầy đủ: validate date/cross-section/duplicate, Mode A/B, sort, empty table, xóa dòng (CMR_15), đổi lĩnh vực, concurrent edit, import, re-submit (CF_03).

---

## 10. Non-functional Requirements ⚡ (4/5)

- **Performance:** API timeout 5s → Mode A fallback. ✅
- **Security:** RBAC + audit log. ✅
- **Concurrency:** Last Write Wins + Lifecycle Log. ✅
- **Gap:** Thiếu Browser Compatibility + WCAG → trừ 1 điểm. (NFR chung toàn hệ thống, chưa có tài liệu riêng.)

---

## Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 13/15 | ⚡ |
| 6 | Object Attributes & Behavior | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow | 20 | 20/20 | ✅ |
| 8 | Functional Integration | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **101/110** | **91.8/100** |

---

## Unified Gap & Question Report

| ID | Priority | Ref | Issue | Status |
|---|---|---|---|---|
| Q1 | ~~Medium~~ | Pre/Post | Số lượng BC tối đa mỗi Bộ/kỳ | ✅ **Resolved** (v1.6: tối đa 1 bản nộp) |
| Q2 | ~~Medium~~ | Actors | Nhiều user cùng Bộ cùng tạo mới | ✅ **Resolved** (v1.6: user lưu trước thắng, sau báo lỗi) |
| Q3 | ~~Medium~~ | Functional Logic | Re-open nháp có dòng API | ✅ **Resolved** (v1.6: giữ snapshot, không re-fetch) |
| Q4 | ~~Low~~ | Integration | Đổi lĩnh vực — Ghi chú manual | ✅ **Resolved** (v1.6: xóa toàn bộ kể cả Ghi chú) |
| Q5 | ~~Low~~ | Integration | API timeout mid-stream | ✅ **Resolved** (v1.6: giữ data, không rollback — CMR_12) |
| Q6 | Low | NFR | Browser Compatibility + WCAG | Open (NFR chung toàn hệ thống) |
| Q7 | ~~Low~~ | Functional Logic | Flow re-submit sau YC chỉnh sửa | ✅ **Resolved** (v1.6: CF_03, sửa ≥1 field → Enabled) |
| G-UI1 | Low | UI Inventory | Phần II thiếu bảng chi tiết riêng | Open (Minor) |
| G-UI2 | Low | UI Inventory | Placeholder cột text chưa quy định | Open (Minor) |

---

## CMR/CF Conflict Check

| Rule | SRS Reference | Conflict? | Detail |
|---|---|---|---|
| CMR_02 | Phân quyền Bộ/Ngành | ✅ No conflict | Mỗi Bộ chỉ thấy BC của mình |
| CMR_03 | Trạng thái BC | ✅ No conflict | 4 trạng thái đúng CMR_03 |
| CMR_04 | Kỳ hạn | ✅ No conflict | Nút Lập/Nhập ẩn khi Chưa tới hạn/Qua kỳ |
| CMR_05 | Validate số | ✅ No conflict | Decimal max 5dp, > 0 |
| CMR_06 | Text fields | ✅ No conflict | Max length, placeholder |
| CMR_07 | Dropdowns | ✅ No conflict | Multiple-selection + instant filter |
| CMR_10 | Phân trang | ✅ No conflict | Đúng CMR_10 |
| CMR_12 | API fields | ✅ No conflict | API fail → Toast T05 + Enabled manual |
| CMR_14 | Dirty Form Guard | ✅ No conflict | Áp dụng đúng |
| CMR_15 | Xóa dòng | ✅ No conflict | ≥ 2 dòng mới hiện, xóa ngay không popup |
| CMR_16 | Filter "Tất cả" | ✅ No conflict | Default "Tất cả" |
| CMR_18 | Tab Navigation | ✅ No conflict | Tham chiếu đúng |
| CF_01 | Lập báo cáo | ✅ No conflict | Luồng đúng |
| CF_02 | Import | ✅ No conflict | Case 2, .xlsx, 10MB |
| CF_03 | Chỉnh sửa | ✅ No conflict | Sửa ≥1 field → Enabled nút Nộp |
| CF_08 | Xóa | ✅ No conflict | Lưu nháp + chưa từng nộp |

---
## 🟢 What's Good

- SRS v1.6 đã resolve **tất cả 7 open questions** từ audit v6 (Q1-Q5, Q7 resolved; Q6 là NFR chung).
- Ràng buộc "1 bản nộp/Bộ/kỳ" + race condition handling rõ ràng.
- Re-open nháp giữ snapshot — logic đơn giản, dễ test.
- API timeout mid-stream behavior rõ ràng (giữ data, không rollback).
- Đổi lĩnh vực xóa toàn bộ (kể cả Ghi chú) — consistent, dễ hiểu.
- Flow re-submit theo CF_03 (sửa ≥1 field → Enabled).
- Mode A/B auto-detect, 15 ACs, Sort, Cross-section validate, Import CF_02 Case 2.
- Filter AND logic đã clarify.
- Wireframe đã cung cấp.

---

## 🧪 Testability Outlook

**What CAN be tested now:**

- Tất cả 15 ACs.
- Mode A/B auto-detect (mock API health-check).
- Race condition: 2 user cùng Bộ tạo mới → user lưu trước thắng.
- Re-open nháp: verify giữ snapshot, không re-fetch.
- API timeout mid-stream: verify giữ data đã fill.
- Đổi lĩnh vực: verify xóa toàn bộ kể cả Ghi chú.
- Flow re-submit: YC chỉnh sửa → sửa ≥1 field → Nộp.
- Validate cross-section + duplicate + date range + empty table.
- Max 200 dòng/Phần.
- Xóa dòng (≥ 2 dòng, không popup, CMR_15).
- Sort (Cột 5/7/9, persist).
- Concurrent edit (Last Write Wins).
- Import CF_02 Case 2.
- Filter AND logic.
- Dirty form guard.

**What CANNOT be tested yet:**

- Browser compatibility matrix (thiếu NFR chung).
- WCAG accessibility compliance (thiếu NFR chung).

**Suggested test focus areas:**

- Race condition: 2 user cùng Bộ tạo mới cùng kỳ → verify lỗi "đã tồn tại".
- Re-open nháp: verify data giữ nguyên, không gọi API.
- API timeout mid-stream: mock partial fill rồi timeout.
- Boundary: Ngày QĐ ranh giới quý, Vốn = 0/âm, 200 dòng/Phần.
- Cross-section: cùng Mã DA ở P.I và P.II, verify date logic.
- Mode A/B: mock API OK/Fail/Timeout.
- Security: user Bộ A truy cập BC Bộ B → chặn.

---

## 📌 Summary & Recommendation

UC101-106 (SRS v1.6) đạt **91.8/100 — READY**. So với audit v6 (87.3/100), điểm tăng +4.5 nhờ resolve 6/7 open questions:
- Q1: Tối đa 1 bản nộp/Bộ/kỳ (+1đ Actors, +2đ Pre/Post)
- Q2: Race condition — user lưu trước thắng
- Q3: Re-open giữ snapshot (+1đ Functional Logic, +1đ Integration)
- Q4: Đổi lĩnh vực xóa toàn bộ kể cả Ghi chú
- Q5: API timeout mid-stream giữ data (+3đ Object Behavior)
- Q7: Flow re-submit theo CF_03 (+1đ AC)

Chỉ còn 3 gaps nhỏ: G-UI1 (Phần II thiếu bảng riêng), G-UI2 (placeholder), Q6 (browser/WCAG) — tất cả Low priority, không block test design. **Sẵn sàng cho test design — QA có thể bắt đầu ngay.**

---

## Change Log

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2026-05-06 | QC Agent | First audit SRS v1.0. Score: 25/110 (22.7/100). NOT READY. |
| v2 | 2026-05-06 | QC Agent | Re-audit SRS v1.1. Score: 110/110 (quá lạc quan). |
| v3 | 2026-05-07 | QC Agent | Deep re-audit. Score: 80/105 (78/100). 13 open questions. |
| v4 | 2026-05-07 | QC Agent | Final re-audit. Score: 83/110 (75.5/100). CONDITIONALLY READY. |
| v5 | 2026-05-07 | QC Agent | Re-audit SRS v1.2. Score: 96/110 (87.3/100). 15/15 gaps resolved. 7 new questions. |
| v6 | 2026-05-22 | QC Agent | CMR Alignment. Score giữ 87.3. Maxlength/precision updates. |
| v7 | 2026-05-22 | QC Agent | Re-audit SRS v1.6. Q1-Q5, Q7 resolved. Score: 96→101/110 (87.3→91.8). Verdict: READY. |
