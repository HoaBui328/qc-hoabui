# UC149-154: Báo cáo tổng hợp tình hình chuyển giao công nghệ tại TCKT có vốn ĐTNN năm ...... (theo địa bàn tỉnh/thành phố) — Mẫu A.IV.11

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.le2 |
| **Phân hệ** | Quản lý đầu tư nước ngoài vào Việt Nam |
| **Mẫu biểu** | Mẫu A.IV.11 |
| **Loại báo cáo** | Định kỳ năm |
| **Phạm vi báo cáo**           | Không có phạm vi                                              |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Bộ Kế hoạch và Đầu tư (Cục Đầu tư nước ngoài) |
| **Đối tượng lập** | Bộ Khoa học và Công nghệ |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-24 |
| **Phiên bản** | 1.8 |
| **Quy tắc sinh mã báo cáo** | FDI_AIV11_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

> **Lưu ý kiến trúc:** Mẫu A.IV.11 là eForm Grid **Fixed 34 Rows** — bảng cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới. Không cho phép thêm/xóa dòng. **8 cột số liệu** chia 4 nhóm (Cấp mới / Sửa đổi bổ sung / Gia hạn / R&D), mỗi nhóm gồm cặp (Số lượng + Giá trị). Hỗ trợ 2 chế độ:
> - **Mode A (Thủ công)** — Kích hoạt khi API Bộ KH&CN KHÔNG khả dụng (auto-detect). Bảng hiển thị 34 dòng với cột số liệu trống, người dùng tự nhập. RULE-01 vẫn áp dụng.
> - **Mode B (API Bộ KH&CN)** — Kích hoạt khi API khả dụng (auto-detect). Hệ thống auto-fill dữ liệu vào các dòng tương ứng. **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh sau khi API điền. RULE-01 áp dụng real-time sau fill.
> - **Cơ chế chuyển đổi:** Auto-detect, **không có toggle/switch trên UI**.
> - **RULE-01:** Khi Số lượng = 0 → Giá trị tự động = 0 và Disabled; khi Số lượng > 0 → Giá trị Enabled. Trigger: **on-blur** cột Số lượng, **debounce 300ms**.

---

## Quy ước RULE-01 — Cross-field Số lượng ↔ Giá trị

Áp dụng cho toàn bộ 4 cặp (Số lượng / Giá trị) trong bảng:

| Điều kiện | Hành vi |
| --- | --- |
| Người dùng nhập / API điền **Số lượng = 0** | Hệ thống tự động set **Giá trị = 0** và **Disabled** (không cho nhập). |
| Người dùng nhập / API điền **Số lượng > 0** | Hệ thống mở **Giá trị sang Enabled** — người dùng nhập giá trị tiền tệ. |
| Người dùng xóa / đổi Số lượng → 0 | Hệ thống reset Giá trị = 0 và Disabled lại. |
| Validate khi Nộp | Nếu Số lượng > 0 mà Giá trị để trống hoặc = 0 → Lỗi inline (🔴 đỏ, **chặn nộp**): "Giá trị phải lớn hơn 0 khi Số lượng > 0". |

**Trigger:** RULE-01 kích hoạt khi người dùng rời khỏi ô Số lượng.

---

## UC149-154.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tổng hợp tình hình CGCN tại TCKT có vốn ĐTNN năm theo địa bàn (Mẫu A.IV.11)
- Chức năng cho phép Bộ Khoa học và Công nghệ truy cập danh sách báo cáo định kỳ năm, được nhóm theo từng Kỳ hạn báo cáo. Mục tiêu: Tổng hợp tình hình chuyển giao công nghệ và đầu tư R&D tại các doanh nghiệp FDI theo địa bàn.
- Out of scope: Không cho phép nộp báo cáo trễ hạn. Việc duyệt báo cáo được thực hiện ở một UC riêng biệt.

Phân quyền: Bộ Khoa học và Công nghệ.

**Tiền điều kiện (Preconditions):**
- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Bộ Khoa học và Công nghệ.
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn".

**Hậu điều kiện (Postconditions):**
- Sau khi Nộp báo cáo thành công, hệ thống gửi thông báo (Notification) cho đơn vị cấp trên (Cục ĐTNN).
- Các thao tác Thêm, Sửa, Xóa đều được hệ thống ghi nhận lịch sử (Audit log).

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo tổng hợp tình hình CGCN (Mẫu A.IV.11)

Chức năng đáp ứng usecase số: 149, 150, 151, 152, 153, 154

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Periodic-single**: Giao diện mẫu cho báo cáo có kỳ hạn năm và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm báo cáo | Yearpicker | Năm hiện tại | x | | Chọn năm; lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ hạn | Multiple-selection Dropdown | Tất cả | x | | Người dùng chọn một hoặc nhiều giá trị: Tất cả / Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07., CMR_16 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Tất cả | x | | Người dùng chọn một hoặc nhiều giá trị: Tất cả / Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Tìm theo mã báo cáo. Hiển thị ngay khi nhập. Nếu không tìm thấy: "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | VD: "Năm 2026". Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ | Label | Null | | | Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Tham chiếu: CMR_09. |
| 10 | Địa bàn | Label | Null | | | Tỉnh/TP của cơ quan lập báo cáo. |
| 11 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 12 | Trạng thái báo cáo | Label | Null | | | Tham chiếu: CMR_03. |
| 13 | Hành động | Button group | Null | | | Chi tiết tham chiếu: UC149-154.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống nhóm theo Kỳ hạn năm. Mặc định collapse; sắp xếp giảm dần. Tham chiếu: CMR_10.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07.
- Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Tham chiếu: CF_01, CMR_04.

---


## UC149-154.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo tổng hợp tình hình CGCN tại TCKT có vốn ĐTNN năm theo địa bàn (Mẫu A.IV.11)
- Chức năng cho phép nhập liệu theo biểu mẫu A.IV.11. Báo cáo là eForm Grid **Fixed 34 Rows** — bảng cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới, 8 cột số liệu chia 4 nhóm với RULE-01 (Số lượng = 0 → Giá trị Disabled). Bảng dữ liệu hỗ trợ 2 chế độ:
  - **Mode A (Thủ công)** — Kích hoạt khi API Bộ KH&CN KHÔNG khả dụng (auto-detect). Bảng hiển thị 34 dòng với cột số liệu trống, user tự nhập. RULE-01 vẫn áp dụng.
  - **Mode B (API Bộ KH&CN)** — Kích hoạt khi API khả dụng (auto-detect). Hệ thống auto-fill dữ liệu vào các dòng tương ứng. **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh. RULE-01 áp dụng real-time sau fill.
  - **Cơ chế chuyển đổi:** Auto-detect, **không có toggle/switch trên UI**.
  - Tham chiếu: CF_01.

Phân quyền: Bộ Khoa học và Công nghệ.

Truy cập chức năng: Màn danh sách báo cáo (UC149-154.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 149, 150

---

### 2. Mô tả giao diện

**Giao diện thêm mới**

Giao diện: Màn hình tạo mới theo biểu mẫu A.IV.11.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN HEADER** | | | | | | |
| 1 | Năm báo cáo | Yearpicker | Năm hiện tại | | x | Hiển thị năm báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Tham chiếu: CMR_05. |
| **BẢNG DỮ LIỆU — FIXED 34 ROWS** | | | | | | Bảng cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới. Không cho phép thêm/xóa dòng. |
| Cột (1) | STT | Integer | Auto | | | Hệ thống tự đánh số 1-34. Disabled. |
| Cột (2) | Tỉnh/Thành phố | Label | Auto | | x | Hiển thị tên 34 tỉnh/TP theo danh mục hành chính sáp nhập mới. **Disabled** — không cho sửa. Sắp xếp theo mã đơn vị hành chính. |
| **Nhóm A — Cấp mới giấy chứng nhận đăng ký chuyển giao công nghệ** | | | | | | Merged header cấp trên. |
| Cột (3) | Số lượng | Integer | Null | x | x | Integer ≥ 0. Max value: 999.999. RULE-01: khi = 0 → Cột (4) Disabled + = 0. **Mode B:** Auto-fill, vẫn **Editable**. Tham chiếu: RULE-01. |
| Cột (4) | Giá trị | Decimal | Null | x* | | Tối đa 5 chữ số thập phân. ≥ 0. Max value: 999.999.999. Editable khi Cột (3) > 0. Disabled và = 0 khi Cột (3) = 0. **Mode B:** Auto-fill, vẫn **Editable**. Placeholder: "Nhập Giá trị (triệu VNĐ)". Tham chiếu: RULE-01, CMR_05. |
| **Nhóm B — Sửa đổi, bổ sung giấy chứng nhận đăng ký chuyển giao công nghệ** | | | | | | Merged header cấp trên. |
| Cột (5) | Số lượng | Integer | Null | x | x | Integer ≥ 0. Max value: 999.999. RULE-01: khi = 0 → Cột (6) Disabled + = 0. **Mode B:** Auto-fill, vẫn **Editable**. |
| Cột (6) | Giá trị | Decimal | Null | x* | | Tối đa 5 chữ số thập phân. ≥ 0. Max value: 999.999.999. Editable khi Cột (5) > 0. Disabled và = 0 khi Cột (5) = 0. **Mode B:** Auto-fill, vẫn **Editable**. Placeholder: "Nhập Giá trị (triệu VNĐ)". Tham chiếu: CMR_05. |
| **Nhóm C — Gia hạn giấy chứng nhận đăng ký chuyển giao công nghệ** | | | | | | Merged header cấp trên. |
| Cột (7) | Số lượng | Integer | Null | x | x | Integer ≥ 0. Max value: 999.999. RULE-01: khi = 0 → Cột (8) Disabled + = 0. **Mode B:** Auto-fill, vẫn **Editable**. |
| Cột (8) | Giá trị | Decimal | Null | x* | | Tối đa 5 chữ số thập phân. ≥ 0. Max value: 999.999.999. Editable khi Cột (7) > 0. Disabled và = 0 khi Cột (7) = 0. **Mode B:** Auto-fill, vẫn **Editable**. Placeholder: "Nhập Giá trị (triệu VNĐ)". Tham chiếu: CMR_05. |
| **Nhóm D — Hoạt động đầu tư cho R&D và trích lập Quỹ Phát triển KH&CN của doanh nghiệp FDI** | | | | | | Merged header cấp trên. |
| Cột (9) | Số lượng | Integer | Null | x | x | Integer ≥ 0. Max value: 999.999. RULE-01: khi = 0 → Cột (10) Disabled + = 0. **Mode B:** Auto-fill, vẫn **Editable**. |
| Cột (10) | Giá trị | Decimal | Null | x* | | Tối đa 5 chữ số thập phân. ≥ 0. Max value: 999.999.999. Editable khi Cột (9) > 0. Disabled và = 0 khi Cột (9) = 0. **Mode B:** Auto-fill, vẫn **Editable**. Placeholder: "Nhập Giá trị (triệu VNĐ)". Tham chiếu: CMR_05. |
| **DÒNG TỔNG CỘNG** | | | | | | Dòng cuối bảng. Disabled. |
| — | Tổng — Cột (3) | Auto-calc | — | | | SUM toàn bộ cột (3). Integer. Real-time. |
| — | Tổng — Cột (4) | Auto-calc | — | | | SUM toàn bộ cột (4). Tối đa 5 chữ số thập phân. Real-time. |
| — | Tổng — Cột (5) | Auto-calc | — | | | SUM toàn bộ cột (5). Integer. Real-time. |
| — | Tổng — Cột (6) | Auto-calc | — | | | SUM toàn bộ cột (6). Tối đa 5 chữ số thập phân. Real-time. |
| — | Tổng — Cột (7) | Auto-calc | — | | | SUM toàn bộ cột (7). Integer. Real-time. |
| — | Tổng — Cột (8) | Auto-calc | — | | | SUM toàn bộ cột (8). Tối đa 5 chữ số thập phân. Real-time. |
| — | Tổng — Cột (9) | Auto-calc | — | | | SUM toàn bộ cột (9). Integer. Real-time. |
| — | Tổng — Cột (10) | Auto-calc | — | | | SUM toàn bộ cột (10). Tối đa 5 chữ số thập phân. Real-time. |
| **PHẦN FOOTER** | | | | | | |
| — | Nơi lập báo cáo | Text/Label | Auto | | | Disabled. Hệ thống tự điền tên tỉnh/TP theo địa chỉ trụ sở cơ quan đăng nhập. Không cho sửa. |
| — | Ngày, tháng, năm lập báo cáo | Date/Label | Auto | | | Disabled. Hệ thống tự điền ngày hiện tại (Current System Date). Định dạng: dd/MM/yyyy. Không cho sửa. |
| **Các Button** | | | | | | |
|  | | — | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
|  | | - | Xem trước | Button | | | | Mở popup PDF Preview báo cáo. Tham chiếu: CF_07.1. |
|  | | — | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
|  | | — | Nộp báo cáo | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

> *`x*` = Editable có điều kiện (chỉ khi Số lượng tương ứng > 0, theo RULE-01).*

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CF_04 (Xuất báo cáo), CF_05 (In), CMR_18.

**Xử lý đặc thù Mẫu A.IV.11:**

A. Cơ chế chuyển đổi Mode A/B (Auto-detect):
- Khi mở form [Lập báo cáo] → hệ thống gọi health-check API Bộ KH&CN.
- API OK → **Mode B** kích hoạt (auto-fill dữ liệu vào các dòng tương ứng, tất cả vẫn Editable).
- API Fail/Timeout → **Mode A** kích hoạt + Toast T05. Tham chiếu: CMR_12. Bảng hiển thị 34 dòng với cột số liệu trống.
- **Không có toggle/switch trên UI**. Không chuyển Mode giữa phiên.

B. Mode A — Nhập tay (Manual Mode):
- Bảng hiển thị cố định 34 dòng. Cột Địa phương đã điền sẵn (Disabled).
- Người dùng nhập trực tiếp 8 cột số liệu cho từng dòng.
- RULE-01 áp dụng real-time (on-blur, debounce 300ms).
- Dòng Tổng cộng cập nhật real-time.

C. Mode B — API Bộ KH&CN:
- **Nhóm A–C (Cấp mới, Sửa đổi bổ sung, Gia hạn):**
  - Nguồn: Hệ thống Giấy chứng nhận đăng ký CGCN của Bộ KH&CN.
  - Logic: API quét Giấy CGCN → đối chiếu Mã DN/Dự án với GCNĐKĐT nội bộ → rút Địa điểm thực hiện → Group By tỉnh/TP → COUNT Số lượng + SUM Giá trị hợp đồng.
- **Nhóm D (R&D):**
  - Nguồn: Cơ sở dữ liệu chi phí/quỹ R&D của Bộ KH&CN.
  - Logic: Đếm số DN FDI có phát sinh chi phí/trích lập quỹ R&D → Group By tỉnh/TP → COUNT Số lượng + SUM Giá trị.
- Auto-fill cột (3)–(10) vào dòng tương ứng.
- **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh giá trị sau khi API điền. User chịu trách nhiệm cuối cùng về tính chính xác.
- Tỉnh/TP không có dữ liệu từ API → cột số liệu để trống, user tự nhập nếu cần.
- RULE-01 áp dụng real-time sau fill.
- Dòng Tổng SUM toàn bộ dòng.

D. Sort:
- Các cột hỗ trợ sort: C3, C4, C5, C6, C7, C8, C9, C10 (tất cả cột số liệu).
- Icon sort hiển thị trên header các cột trên. Click icon → toggle: Ascending ↑ / Descending ↓.
- **Mặc định sort:** C4 (Cấp mới CGCN — Giá trị) Descending (max → min).
- Dòng Tổng luôn ở cuối bảng, không tham gia sort.
- Sort persist khi Lưu nháp → mở lại giữ nguyên thứ tự.
- Mode B: hệ thống auto-sort theo default sort (C4 Descending) trước khi render.

E. RULE-01 — Cross-field Số lượng → Giá trị:
- Trigger: **on-blur** cột Số lượng, **debounce 300ms**.
- Áp dụng cho 4 cặp: (3)→(4), (5)→(6), (7)→(8), (9)→(10).
- Số lượng = 0 → Giá trị = 0 + Disabled. Số lượng > 0 → Giá trị Enabled.
- Khi người dùng thay đổi Số lượng từ > 0 về 0: reset Giá trị = 0 + Disabled.

F. Validate khi Nộp:
- Tất cả cột Số lượng (3, 5, 7, 9) phải có giá trị (không trống). Integer ≥ 0.
- Cột Giá trị (4, 6, 8, 10): tối đa 5 chữ số thập phân, ≥ 0.
- Nếu Số lượng > 0 mà Giá trị để trống hoặc = 0 → lỗi inline (🔴 đỏ, **chặn nộp**): "Giá trị phải lớn hơn 0 khi Số lượng > 0". Dừng luồng.
- Vi phạm validate bắt buộc → lỗi inline, dừng luồng. Tham chiếu: CF_01.
- **Hiển thị lỗi trong eForm Grid:** Lỗi hiển thị dạng **viền đỏ** quanh ô; hover vào ô hiển thị **tooltip** chứa message lỗi tương ứng. Tham chiếu: CMR_05, CMR_06, CMR_07.
- Nộp thành công → trạng thái "Chờ duyệt".

G. Nhập từ file: CF_02 — **Case 2** (không có Phạm vi). .xlsx only, max 10MB. Sau khi Import thành công, hệ thống evaluate RULE-01 cho toàn bộ 34 dòng ngay lập tức (không chờ on-blur).

H. Dòng Tổng cộng: Cập nhật real-time từng cột độc lập khi thay đổi bất kỳ ô nào. Disabled.

I. Footer: Nơi lập báo cáo và Ngày tháng năm tự động từ hệ thống. Disabled.

- Xuất báo cáo: Kết xuất file **Excel**. Tham chiếu: CF_04.

---


## UC149-154.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi.

Phân quyền: Kiểm soát theo trạng thái bản ghi. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC149-154.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 151, 152, 153, 154

---

### 2. Mô tả giao diện

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Kết xuất file Excel. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file **Excel**. Tham chiếu: CF_04.
- Chỉnh sửa báo cáo: Tham chiếu: CF_03.

---

## 3.4 Acceptance Criteria (Tiêu chí nghiệm thu)

- **AC1 Fixed 34 Rows:** Khi vào màn hình "Lập báo cáo", bảng luôn hiển thị cố định 34 dòng tương ứng 34 tỉnh/TP theo danh mục hành chính sáp nhập mới. Không cho phép thêm/xóa dòng.
- **AC2 Mode Detect:** Mở form → health-check API Bộ KH&CN. API OK → Mode B (auto-fill, Editable). API Fail → Mode A (bảng 34 dòng trống) + Toast T05. Tham chiếu: CMR_12.
- **AC3 API Bộ KH&CN (Mode B):** Auto-fill cột (3)–(10) cho các dòng tỉnh/TP có dữ liệu. Tất cả dữ liệu vẫn Editable — user có thể hiệu chỉnh.
- **AC4 Tỉnh/TP Disabled:** Cột Địa phương = Label, Disabled. User không thể sửa tên tỉnh/TP.
- **AC5 RULE-01 Real-time:** Khi nhập Số lượng = 0 tại bất kỳ cột nào (3, 5, 7, 9) → Hệ thống tự động reset Giá trị tương ứng = 0 và Disable ô đó ngay lập tức. Khi Số lượng > 0 → Enable ô Giá trị. Trigger: on-blur, debounce 300ms.
- **AC6 SUM Real-time:** Dòng Tổng cộng của 8 cột số liệu phải cập nhật real-time khi thay đổi bất kỳ ô nào.
- **AC7 Validate Giá trị:** Khi nhấn "Nộp báo cáo", nếu có dòng nào có Số lượng > 0 mà Giá trị = 0 hoặc trống → Hiển thị lỗi inline (🔴 viền đỏ + tooltip) "Giá trị phải lớn hơn 0 khi Số lượng > 0" và **chặn nộp**. Tham chiếu: CMR_05.
- **AC8 Validate bắt buộc:** Tất cả cột Số lượng (3, 5, 7, 9) phải được điền giá trị (≥ 0). Nếu trống → Báo lỗi inline và chặn nộp.
- **AC9 Decimal precision:** Cột Giá trị (4, 6, 8, 10): tối đa 5 chữ số thập phân. Cột Số lượng (3, 5, 7, 9): integer.
- **AC10 Max value:** Cột Số lượng max 999.999. Cột Giá trị max 999.999.999.
- **AC11 Placeholder:** Cột Giá trị (4, 6, 8, 10) hiển thị placeholder "Nhập Giá trị (triệu VNĐ)". Tham chiếu: CMR_05.
- **AC12 Sort:** Icon sort hiển thị trên header C3, C4, C5, C6, C7, C8, C9, C10 (tất cả cột số liệu). Click → toggle Ascending/Descending. Mặc định: C4 Descending (max → min). Dòng Tổng luôn ở cuối. Sort persist khi Lưu nháp.
- **AC13 Footer tự động:** Nơi lập và Ngày lập Disabled, điền tự động.
- **AC14 Concurrent Edit:** Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác được ghi vào Lifecycle Log. Tham chiếu: CF_06.
- **AC15 Nộp thành công:** Trạng thái "Chờ duyệt".
- **AC16 eForm Grid Error Display:** Lỗi validate trong bảng eForm Grid hiển thị dạng **viền đỏ** quanh ô lỗi; hover vào ô hiển thị **tooltip** chứa message lỗi tương ứng (không hiển thị text inline dưới ô do không gian hạn chế). Tham chiếu: CMR_05, CMR_06, CMR_07.
- **AC17 Tab Navigation:** Nhấn Tab chuyển focus sang ô kế tiếp theo thứ tự trái→phải, trên→dưới (chỉ áp dụng cho ô Enabled). Shift+Tab quay lại ô trước đó. Tham chiếu: CMR_18.

---

## 3.5 Non-Functional Requirements (Yêu cầu phi chức năng)

- **Performance:** Thời gian gọi API Bộ KH&CN và render Grid 34 dòng không quá 5 giây. Nếu quá 5s → Toast T05 (Tham chiếu: CMR_12) + Enable toàn bộ ô cho nhập thủ công.
- **Security & Audit:** Chỉ Bộ KH&CN mới có quyền lập báo cáo. Lưu vết Audit log đầy đủ cho mọi hành động.
- **Concurrency:** Áp dụng Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác đều được ghi vào Lifecycle Log (Actor, Action, Timestamp). Tham chiếu: CF_06.
- **Accessibility & Navigation:** Hỗ trợ Tab/Shift+Tab navigation trong eForm Grid. Tham chiếu: CMR_18.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Thông tin chung | (Không có) | Thêm Mục tiêu, Phạm vi, Tiền kiện, Hậu kiện. | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.0 → 1.1 | Tiêu chí nghiệm thu | (Không có) | Bổ sung 6 AC chi tiết cho luồng chuyển giao công nghệ. | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.0 → 1.1 | Yêu cầu phi chức năng | (Không có) | Bổ sung NFR (Performance, Security). | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.1 → 1.2 | Phiên bản | 1.1 | 1.2 | Cập nhật sau QC Re-Audit Round 2. |
| 2026-05-07 | 1.2 | Kiến trúc | Read-only / Editable sau fill | Mode A/B auto-detect — Mode B: Editable sau fill + RULE-01 real-time; Mode A: Enabled toàn bộ | QC Audit — sửa API deadlock, rõ Mode. |
| 2026-05-07 | 1.2 | Bảng dữ liệu | Decimal Giá trị | Integer 0dp triệu VND, max 999.999 (Số lượng) / 999.999.999 (Giá trị), sắp theo mã đơn vị hành chính | QC Audit — decimal precision + max value. |
| 2026-05-07 | 1.2 | RULE-01 | Real-time (không rõ trigger) | On-blur cột Số lượng, debounce 300ms | QC Audit — chi tiết trigger. |
| 2026-05-07 | 1.2 | Xử lý | 3 mục cơ bản | A-K (Mode detect, Mode A, Mode B, API Partial, RULE-01, All zeros valid, Validate, Nhập từ file, Tổng, Footer) | QC Audit — viết lại. |
| 2026-05-07 | 1.2 | Warning UI | Inline | Yellow banner ⚠️ cho all-zeros + Giá trị chưa xác định | QC Audit — UI chuẩn hóa. |
| 2026-05-07 | 1.2 | AC | AC1-AC6 | AC1-AC16 (Mode detect, API partial, decimal, max, all zeros, nhập từ file, concurrent) | QC Audit — bổ sung AC. |
| 2026-05-07 | 1.2 | NFR | Performance, Security | Thêm Concurrency | QC Audit — concurrent edit. |
| 2026-05-11 | 1.0→1.1 | Quy tắc sinh mã báo cáo | `DTNN_A4_11_[ID]` | `FDI_AIV11_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1 | Label Trạng thái kỳ | `Trạng thái (cấp kỳ)` | `Trạng thái kỳ` | Chuẩn hóa tên label (INS-06) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-11 | 1.2 → 1.3 | Toast T05 (Mode A fallback) | Nội dung toast tự viết | Tham chiếu CMR_12 (T05 chuẩn) | QC Feedback — chuẩn hóa toast. |
| 2026-05-11 | 1.2 → 1.3 | Mục E (API Partial Failure) | Có mục + AC6 + toast warning | Xóa — không có cơ chế phát hiện data thiếu/đủ | QC Feedback — logic không khả thi. |
| 2026-05-11 | 1.2 → 1.3 | AC | AC1-AC16 (có AC6 API Partial) | AC1-AC15 (bỏ AC6, đánh lại số) | QC Feedback — đồng bộ với xóa mục E. |
| 2026-05-11 | 1.2 → 1.3 | AC14 + NFR Concurrency | Optimistic locking — conflict + refresh | Last Write Wins theo CMR_02 — thao tác sau ghi đè, cả 2 ghi Lifecycle Log | QC Feedback — đồng bộ CMR_02, CF_06. |
| 2026-05-12 | 1.3 → 1.4 | Kiến trúc | Cố định 63 dòng | Dynamic Rows — Mode B chỉ sinh dòng có dữ liệu, dòng API cột Tỉnh/TP Disabled, user thêm manual | Client confirm: chỉ tỉnh có số thì báo cáo. |
| 2026-05-12 | 1.4 | Bảng dữ liệu | 63 dòng cố định, Địa phương = Text/Label | Dynamic Rows, Địa phương = Dropdown auto-filter, thêm [+ Thêm dòng] + Xóa dòng | Đồng bộ kiến trúc Dynamic Rows. |
| 2026-05-12 | 1.4 | Xử lý Mode A | Load sẵn 63 dòng, user nhập cột (3)–(10) | Bảng trống, user thêm dòng + chọn Tỉnh/TP từ dropdown | Dynamic Rows. |
| 2026-05-12 | 1.4 | Xử lý Mode B | Auto-fill 63 dòng, tất cả Editable | Auto-generate N dòng (chỉ tỉnh có data), cột Tỉnh/TP Disabled, cột số liệu Editable, user thêm manual | Dynamic Rows. |
| 2026-05-12 | 1.4 | Mục G (All 63 = 0) | Edge case cho phép nộp + Warning | Xóa — không còn 63 dòng cố định | Dynamic Rows — validate ≥ 1 dòng thay thế. |
| 2026-05-12 | 1.4 | Nhập từ file | Template pre-fill 63 dòng; ≠ 63 → lỗi | Bỏ ràng buộc 63 dòng | Dynamic Rows. |
| 2026-05-12 | 1.4 | AC | AC1-AC15 (fixed 63 rows) | AC1-AC16 (Dynamic Rows, unique, empty table, xóa dòng) | Viết lại AC cho Dynamic Rows. |
| 2026-05-14 | 1.4 → 1.5 | Kiến trúc bảng | Dynamic Rows — chỉ sinh dòng cho tỉnh/TP có dữ liệu | Fixed 34 Rows — 34 tỉnh/TP theo danh mục sáp nhập mới, không thêm/xóa dòng | Client confirm: chuyển sang 34 tỉnh sáp nhập. |
| 2026-05-14 | 1.5 | Cột Địa phương | Dropdown (chọn từ 63 tỉnh/TP, unique, auto-filter) | Label (Disabled, pre-filled 34 tỉnh/TP) | Fixed 34 Rows. |
| 2026-05-14 | 1.5 | Cột Giá trị (4, 6, 8, 10) | 0dp integer triệu VND | Tối đa 5 chữ số thập phân + Placeholder "Đơn vị: VNĐ" | Client feedback — tăng precision + placeholder. |
| 2026-05-14 | 1.5 | Dòng API | Cột Tỉnh/TP Disabled, có tag "API" | Bỏ tag "API", tất cả Editable (cột Địa phương Disabled do Fixed 34) | Client feedback — user chịu trách nhiệm cuối cùng. |
| 2026-05-14 | 1.5 | Sort | Không có | Icon sort C3, C4, C5, C6. Mặc định: C4 Descending (max → min) | Client feedback — thêm sort. |
| 2026-05-14 | 1.5 | Thêm/Xóa dòng | [+ Thêm dòng] + icon Xóa dòng manual | Xóa — bảng cố định 34 dòng | Fixed 34 Rows. |
| 2026-05-14 | 1.5 | AC | AC1-AC16 (Dynamic Rows, unique, empty table, xóa dòng) | AC1-AC15 (Fixed 34, Editable, Sort, Placeholder, 5dp) | Viết lại AC cho Fixed 34 Rows. |
| 2026-05-14 | 1.5 → 1.6 | Filter Địa bàn (danh sách) | Có filter Địa bàn (row #2) | Xóa — báo cáo đơn lẻ, không cần lọc theo địa bàn | QC Review. |
| 2026-05-14 | 1.6 | Năm báo cáo (form Lập) | Editable, validate 4 chữ số | Disabled — hiển thị năm đã chọn từ màn danh sách | QC Review — năm đã chọn ở màn danh sách, không cần nhập lại. |
| 2026-05-14 | 1.6 | RULE-01 Validate | Warning only (không chặn nộp) khi Số lượng > 0 mà Giá trị = 0 | Hard validate — chặn nộp, lỗi inline đỏ | QC Review — Số lượng > 0 thì Giá trị phải > 0. |
| 2026-05-14 | 1.6 | Tên cột (header) | Rút gọn: "Cấp mới", "Sửa đổi, bổ sung", "Gia hạn", "R&D" | Đầy đủ theo template: "Cấp mới giấy chứng nhận đăng ký CGCN", "Sửa đổi, bổ sung giấy chứng nhận đăng ký CGCN", "Gia hạn giấy chứng nhận đăng ký CGCN", "Hoạt động đầu tư cho R&D và trích lập Quỹ Phát triển KH&CN của DN FDI" | QC Review — đồng bộ template. |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | STD-04a Custom Placeholder | 4 truong khong chuan | Dong bo Nhap [ten truong] (Goi y) | CMR_06 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-21 | 1.6 → 1.7 | RULE-01 Validate khi Nộp (mục F + AC7) | Warning yellow, không chặn nộp — "Giá trị chưa xác định" | Hard validate — chặn nộp, lỗi inline đỏ viền đỏ + tooltip — "Giá trị phải lớn hơn 0 khi Số lượng > 0". Tham chiếu: CMR_05 | Đồng bộ Changelog v1.6 (đã ghi hard validate nhưng mục F + AC7 chưa cập nhật) |
| 2026-05-21 | 1.6 → 1.7 | eForm Grid Error Display | Không có mô tả cách hiển thị lỗi trong grid | Bổ sung: Lỗi trong eForm Grid hiển thị dạng viền đỏ + tooltip (không text inline). Tham chiếu: CMR_05, CMR_06, CMR_07 | Đồng bộ CMR v2.4 |
| 2026-05-21 | 1.6 → 1.7 | Tab Navigation (AC17 + NFR) | Không có | Bổ sung AC17: Tab/Shift+Tab navigation trong eForm Grid. NFR: Accessibility. Tham chiếu: CMR_18 | Đồng bộ CMR v2.0 |
| 2026-05-21 | 1.6 → 1.7 | Placeholder cột Giá trị | "Nhập Giá trị (triệu VNĐ) (Đơn vị: VNĐ)" (bảng) vs "Đơn vị: VNĐ" (AC11) | Thống nhất: "Nhập Giá trị (triệu VNĐ)" — cả bảng giao diện và AC11 | Chuẩn hóa theo CMR_05 placeholder rule |
| 2026-05-21 | 1.6 → 1.7 | Sort (mục D + AC12) | Icon sort chỉ C3, C4, C5, C6 | Icon sort C3–C10 (tất cả cột số liệu). Mặc định C4 Descending | BA xác nhận: sort áp dụng cho tất cả cột số |
| 2026-05-22 | 1.7 → 1.8 | Phân quyền — Bỏ CMR_02 | Tham chiếu: CMR_02 tại các mục Phân quyền + AC14 + NFR | Xóa tham chiếu CMR_02 — CMR_02 dành cho NĐT trong dự án, không phù hợp cho cơ quan ban ngành (Bộ KH&CN) | BA xác nhận: CMR_02 không áp dụng |
| 2026-05-22 | 1.7 → 1.8 | RULE-01 sau Import (mục G) | Không mô tả hành vi RULE-01 sau Import | Bổ sung: Sau Import thành công, hệ thống evaluate RULE-01 cho toàn bộ 34 dòng ngay lập tức (không chờ on-blur) | BA xác nhận: theo common rule Import |
