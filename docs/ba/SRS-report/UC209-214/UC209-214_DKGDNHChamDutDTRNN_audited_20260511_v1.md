# Báo cáo Audit Mức Độ Sẵn Sàng (QA Readiness Report)

**Tài liệu đánh giá:** `UC209-214_DKGDNHChamDutDTRNN.md`  
**Người đánh giá:** Antigravity (AI Agent)  
**Ngày đánh giá:** 2026-05-11  

---

## Phần 1: Đánh giá Điểm số (Scorecard)

| # | Knowledge Area | Max Pts | Score | Status |
| --- | --- | --- | --- | --- |
| 1 | Feature Identity (Tiêu đề, ID, Context) | 5 | 5/5 | ✅ |
| 2 | Objective & Scope (Mục tiêu & Phạm vi) | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles (Vai trò người dùng) | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions (Tiền/Hậu điều kiện) | 10 | 8/10 | ⚡ |
| 5 | UI Object Inventory & Mapping (Danh mục UI) | 15 | 13/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition (Hành vi đối tượng) | 20 | 16/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition (Luồng chức năng) | 20 | 16/20 | ⚡ |
| 8 | Functional Integration Analysis (Tích hợp chức năng) | 10 | 8/10 | ⚡ |
| 9 | Acceptance Criteria (Tiêu chí nghiệm thu) | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements (Phi chức năng) | 5 | 0/5 | ⚠️ |
| **Total** | | **110** | **91/110** | **82.7/100** |

**Verdict: ⚠️ CONDITIONALLY READY** (82.7/100)

---

## Phần 2: Đánh giá chi tiết các vùng kiến thức

### 0. Feature Identity ✅
- **Mã UC:** UC209-214
- **Tên báo cáo:** Báo cáo về tình hình đăng ký giao dịch ngoại hối và chấm dứt hoạt động đầu tư ra nước ngoài (Mẫu II.5)
- **Chu kỳ báo cáo:** Định kỳ (Tháng) — 12 kỳ/năm
- **Quy tắc sinh mã báo cáo:** `ODI_II5_[ID]`

### 1. Objective & Scope ✅
- **Phạm vi đầu vào:** Không có phạm vi.
- **Cơ quan nhận:** Bộ Tài chính (Cục Đầu tư nước ngoài).

### 2. Actors & User Roles ✅
- **Đối tượng lập:** Ngân hàng Nhà nước Việt Nam. Phân quyền người tạo theo **CMR_03**. 
- Mỗi tài khoản chỉ thấy bản ghi do mình tạo ở màn danh sách. Không áp dụng CMR_01, CMR_02.

### 3. Preconditions & Postconditions ⚡
- **Preconditions:** Cán bộ có tài khoản Admin Site. Kỳ hạn "Trong thời hạn" (CMR_04) để lập báo cáo.
- **Postconditions:** Thay đổi trạng thái bản ghi theo **CMR_03**. 
- *(Gap):* Thiếu đề cập áp dụng chuẩn format "Số văn bản" (CMR_13).

### 4. UI Object Inventory & Mapping ⚡
*Danh sách chi tiết các thành phần UI dựa trên thiết kế.*

**Màn hình Danh sách (Periodic-single)**
| Component Name | Component Type | Required | Default / Enum Values |
| --- | --- | --- | --- |
| Năm | Yearpicker | | Năm hiện tại |
| Trạng thái kỳ hạn | Multiple-selection Dropdown | | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo |
| Trạng thái báo cáo | Multiple-selection Dropdown | | Lưu nháp / Chờ duyệt / Đã tiếp nhận / YC chỉnh sửa |
| Mã báo cáo | Search bar | | Placeholder: "Nhập dữ liệu" |
| Năm báo cáo | Label (collapsible) | | VD: "Năm 2026", Mặc định collapse |
| Kỳ tháng | Label | | Tháng 1 đến Tháng 12 |
| Trạng thái kỳ hạn (nhãn) | Label | | |
| Lập báo cáo | Button | | Chỉ hiển thị khi "Trong thời hạn" |
| Import | Button | | Chỉ hiển thị khi "Trong thời hạn" |
| Mã báo cáo (trong danh sách) | Label | | `ODI_II5_[ID]` |
| Ngày cập nhật | Label | | dd/MM/yyyy HH:mm |
| Trạng thái | Label | | Theo CMR_03 |
| Hành động | Button group | | Xem, Sửa, Nộp, Vòng đời, In, Export, Xóa |

**Màn hình Lập báo cáo / Chỉnh sửa**
| Component Name | Component Type | Required | Default / Enum Values |
| --- | --- | --- | --- |
| Đơn vị lập | Label | | "Ngân hàng Nhà nước Việt Nam" |
| Số văn bản | Textbox | * | Placeholder: "Nhập dữ liệu" |
| Kỳ báo cáo | Label | | VD: "Tháng 3 Quý I Năm 2026" |
| **Bảng 1** | | | |
| Bảng 1 - STT | Number | | Auto-increment |
| Bảng 1 - Tên NĐT | Textbox | * | |
| Bảng 1 - Mã số DN / CCCD | Textbox | * | |
| Bảng 1 - Mã số ĐKGDNH | Textbox | * | |
| Bảng 1 - Địa chỉ trụ sở | Textbox | * | |
| Bảng 1 - Hình thức ĐT | Dropdown | * | Thành lập TCKT / Góp vốn mua CP / Mua phần vốn góp / Đầu tư theo HĐ / Hình thức khác |
| Bảng 1 - Mục tiêu HĐ | Textbox | * | |
| Bảng 1 - Vốn ĐTRNN (USD) | Number | * | > 0; 2 chữ số thập phân |
| Bảng 1 - Quốc gia/vùng lãnh thổ| Dropdown | * | Danh mục quốc gia chuẩn từ hệ thống |
| Bảng 1 - Dòng Tổng Vốn | Calculated | | Auto-sum |
| Bảng 1 - [Thêm hàng] | Button | | |
| Bảng 1 - [Xóa hàng] | Button | | |
| **Bảng 2** | | | |
| Bảng 2 - STT | Number | | Auto-increment |
| Bảng 2 - Tên NĐT | Textbox | * | |
| Bảng 2 - Mã số DN / CCCD | Textbox | * | |
| Bảng 2 - Mã số ĐKGDNH | Textbox | * | |
| Bảng 2 - Địa chỉ trụ sở | Textbox | * | |
| Bảng 2 - Hình thức ĐT | Textbox | * | Nhập tay tự do (freetext) *(Mâu thuẫn với Bảng 1)* |
| Bảng 2 - Mục tiêu HĐ | Textbox | * | |
| Bảng 2 - Vốn đã chuyển ra NN | Number | * | ≥ 0; 2 chữ số thập phân |
| Bảng 2 - Quốc gia/vùng lãnh thổ| Dropdown | * | Danh mục quốc gia chuẩn từ hệ thống |
| Bảng 2 - Dòng Tổng Vốn | Calculated | | Auto-sum |
| Bảng 2 - [Thêm hàng] | Button | | |
| Bảng 2 - [Xóa hàng] | Button | | |
| **Mục 3 & Hành động** | | | |
| Đề xuất, kiến nghị | Textarea | | Max 1000 ký tự |
| Lưu nháp | Button | | |
| Xem | Button | | Popup PDF Preview |
| Nộp báo cáo | Button | | |
| Hủy | Button | | |

*(Gap):* Hình thức ĐT ở Bảng 2 là Textbox nhập freetext trong khi Bảng 1 là Dropdown (enum). Nguồn dữ liệu của Dropdown Quốc gia chưa được đề cập rõ có phải API auto-fill hay tĩnh.

### 5. Object Attributes & Behavior Definition ⚡
| Component | System States | Behavior / Interaction Matrix |
| --- | --- | --- |
| Các Component Lọc | Enabled | Chọn/Nhập -> Auto trigger filter data, không cần nút Submit (CMR_07, CMR_06). |
| Nút [Lập báo cáo], [Import] | Conditional | Chỉ Enabled và hiển thị khi kỳ báo cáo "Trong thời hạn". |
| Đơn vị lập, Kỳ báo cáo, Dòng tổng, STT | Disabled | Không cho phép chỉnh sửa. Dòng tổng auto-sum real-time nền xám. |
| Textbox (Số VB, Tên, Địa chỉ...)| Enabled | Auto-trim khoảng trắng (CMR_06). Bắt buộc phải có giá trị khi Nộp. |
| Vốn ĐTRNN (Bảng 1) | Enabled | Chỉ nhận số, `.`, `,`. Nhập ≤ 0 -> Báo lỗi inline "Giá trị phải lớn hơn 0". |
| Vốn đã chuyển ra NN (Bảng 2)| Enabled | Chỉ nhận số, `.`, `,`. Nhập < 0 -> Báo lỗi ký tự không hợp lệ. Cho phép nhập = 0. |
| Nút [Thêm hàng] | Enabled | Click -> Thêm dòng mới. |
| Nút [Xóa hàng] | Conditional | Ẩn khi chỉ có 1 dòng. Xuất hiện khi >= 2 dòng. Click -> Xóa ngay lập tức không cần xác nhận. |

*(Gap):* "Bảng 1 và Bảng 2 được phép rỗng" nhưng giao diện khởi tạo 1 dòng (tối thiểu 1 dòng). Bảng có 1 dòng rỗng thì ấn Nộp có báo lỗi rỗng ở các ô required trong dòng đó không?

### 6. Functional Logic & Workflow Decomposition ⚡
- **Luồng Lọc (Danh sách):** Tìm kiếm live-search theo Mã báo cáo (Debounce), Năm, Trạng thái. Áp dụng CMR_07.
- **Luồng Tạo mới:** Bấm Lập báo cáo -> Mở form, khởi tạo Đơn vị lập, kỳ báo cáo, 2 bảng mỗi bảng 1 dòng trống. 
- **Luồng Nộp (Submit):** Hệ thống validate các trường bắt buộc (Số văn bản và dữ liệu các bảng nếu có). Bấm Nộp -> Hiển thị Popup xác nhận (Checkbox "Tôi đã kiểm tra..."). Nếu check -> Nộp -> Trạng thái thành Chờ duyệt/Đã tiếp nhận (CMR_03). Toast T02.
- **Luồng Lưu nháp:** Chỉ cần nhập >= 1 trường thông tin là có thể lưu (CF_01). Bấm Lưu nháp -> Toast T01. Trạng thái: Lưu nháp. 
- **Luồng Hủy / Chuyển hướng:** Dirty check, nếu form dirty hiện popup P02 (Dữ liệu chưa được lưu). 
- **Luồng Export / In:** Kết xuất file .docx, In mở Print Dialog của trình duyệt. Tên file theo định dạng chuẩn. Xem chi tiết mở Popup Preview.

### 7. Functional Integration Analysis ⚡
- Tính tổng giá trị vốn ở Bảng 1 và Bảng 2 cập nhật real-time ngay khi người dùng gõ số, tự trừ khi xóa hàng.
- Nút Import có thể lấy template .docx/.xlsx về điền sau đó upload mapping vào các trường trên lưới.

### 8. Acceptance Criteria ✅
*Được tạo tự động từ quy tắc nghiệp vụ.*

**AC1: Validate bắt buộc (CF_01)**
- Given Người dùng vào Màn hình tạo báo cáo
- When Người dùng bấm [Nộp] nhưng để trống Số văn bản
- Then Hệ thống hiển thị lỗi inline đỏ "Trường bắt buộc" ngay dưới Số văn bản và không nộp.

**AC2: Tính hợp lệ của Trường Số Vốn (Bảng 1 & 2)**
- Given Người dùng thêm dòng ở Bảng 1
- When Nhập `0` vào "Vốn ĐTRNN"
- Then Lỗi inline "Giá trị phải lớn hơn 0" hiển thị
- When Nhập `0` vào "Vốn đã chuyển ra NN" ở Bảng 2
- Then Giá trị hợp lệ, không hiển thị lỗi.

**AC3: Tính toán Dòng Tổng**
- Given Bảng 1 có dòng vốn $10,000 và dòng vốn $5,000
- Then Dòng tổng tự động tính $15,000
- When Người dùng bấm Xóa dòng $5,000
- Then Dòng tổng tự động tính lại còn $10,000.

**AC4: Add/Remove Row (CMR_15)**
- Given Bảng 1 đang có 1 dòng
- Then Nút [Xóa hàng] bị ẩn
- When Người dùng bấm [Thêm hàng]
- Then STT tự tăng, dòng 2 hiển thị và nút [Xóa hàng] hiển thị trên cả 2 dòng.

**AC5: Lưu nháp (CF_01)**
- Given Người dùng mở form và chưa nhập gì
- When Người dùng bấm Lưu nháp
- Then Toast lỗi T07 hiển thị: "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp"

### 9. Non-functional Requirements ⚠️
- Không có yêu cầu bảo mật, hiệu năng nào được xác định riêng cho UC này. (Sử dụng phân trang 10 dòng/trang theo CMR_10).

---

## Phần 3: Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
| --- | --- | --- | --- | --- | --- |
| Q1 | High | *Mục 2 - Bảng 1 (Hình thức ĐT: Dropdown) vs Bảng 2 (Hình thức ĐT: Textbox)* | Cột "Hình thức ĐT" ở Bảng 1 là Dropdown (5 options cố định), nhưng ở Bảng 2 lại là Textbox nhập tay tự do. Đây là yêu cầu nghiệp vụ thực tế hay là lỗi đánh máy? | Cần đồng nhất kiểu dữ liệu hoặc hiểu rõ lý do để kiểm thử giá trị đầu vào hợp lệ. | Open |
| Q2 | High | *Mục 3 (Validate khi Nộp): "Bảng 1 và Bảng 2 được phép rỗng... Không bắt buộc ≥ 1 dòng" vs Mục 2: "Tối thiểu 1 dòng"* | UC ghi bảng tối thiểu 1 dòng khởi tạo. Nếu người dùng không nhập gì vào dòng này và bấm Nộp thì hệ thống có bắt lỗi "Trường bắt buộc" cho các ô trong dòng đó không, hay cho phép Nộp bảng với 1 dòng trống? Người dùng có được phép xoá dòng duy nhất đó để bảng có 0 dòng không (do CMR_15 không cho xoá dòng cuối)? | Ảnh hưởng tới test case Nộp báo cáo không phát sinh nghiệp vụ. Tester cần biết kết quả mong đợi khi bấm Nộp với 1 dòng trống. | Open |
| Q3 | High | *Mục 2 - Bảng Danh sách: "Trạng thái báo cáo" có đủ 4 trạng thái* | UC quy định filter có "Chờ duyệt / Đã tiếp nhận". Theo CMR_03, Nộp xong sẽ rẽ nhánh vào 1 trong 2 tùy quy trình (2 bước hoặc >2 bước). Quy trình duyệt nội bộ của Mẫu II.5 gồm mấy bước? Nộp xong chuyển thẳng sang Đã tiếp nhận hay phải qua Chờ duyệt? | Tester không thể thiết kế luồng trạng thái đúng (State Transition) nếu không biết quy trình duyệt. | Open |
| Q4 | Medium | *Mục 2 - Bảng 1 & Bảng 2 (Mã số DN / CCCD)* | Validate hiện tại chỉ là "Không rỗng" (CMR_06). Có cần validate rule đặc thù (VD: chỉ nhập số, độ dài 10-13 cho mã DN, 12 cho CCCD) không? Việc dùng chung 1 trường cho cả mã DN và CCCD dễ dẫn tới dữ liệu rác. | Bổ sung validate để QA có cơ sở bắt lỗi định dạng. | Open |
| Q5 | Medium | *Mục 2 - HEADER (Số văn bản)* | Trường "Số văn bản" có áp dụng bộ quy tắc nhập/định dạng công văn theo chuẩn `CMR_13` không? | Nếu áp dụng CMR_13, cần test các ký tự đặc biệt, auto-uppercase, định dạng dấu `/`, `-`. | Open |
| Q6 | Medium | *Bảng thuộc tính - Cơ quan nhận: Bộ Tài chính (Cục Đầu tư nước ngoài)* | Báo cáo này nộp cho cơ quan ngoài bộ (Bộ Tài chính). Việc Nộp có liên thông/gọi API gửi dữ liệu sang hệ thống của BTC không, hay chỉ lưu nội bộ trên hệ thống MBFS? | Ảnh hưởng đến việc thiết kế test Integration và mô phỏng (mock) API bên thứ 3. | Open |
| Q7 | Medium | *Mục 3 - Mô tả các xử lý chung: "Phân trang theo số năm / trang"* | Ở CMR_10 quy định "List có kỳ hạn: Phân trang theo Kỳ". Báo cáo này nhóm theo năm, mỗi năm có 12 kỳ. Vậy phân trang theo "số năm / trang" nghĩa là 1 trang hiển thị 10 Năm (120 kỳ) hay 10 Kỳ (không chẵn năm)? | Đảm bảo tính nhất quán của giao diện Danh sách. | Open |
| Q8 | Medium | *Mục 2 - Bảng 1 & 2 (Quốc gia / vùng lãnh thổ)* | Trường "Quốc gia / vùng lãnh thổ" lấy "Danh mục quốc gia chuẩn từ hệ thống". Danh mục này được cung cấp qua API (Master Data) hay fix cứng (Static)? | Cần xác nhận để QC lấy đúng danh mục kiểm tra tính đúng đắn khi hiển thị trên Dropdown. | Open |
| Q9 | Low | *Mục 2 - Bảng 1 (Vốn ĐTRNN > 0) vs Bảng 2 (Vốn đã chuyển ra NN ≥ 0)* | Bảng 1 bắt buộc Vốn > 0. Nếu nhập = 0 sẽ báo lỗi "Giá trị phải lớn hơn 0". Bảng 2 bắt buộc Vốn ≥ 0 (tức là cho phép nhập 0). Điều này có chính xác không? | Cần xác nhận mốc biên giới hạn 0 của hai cột này có thực sự khác nhau không để thiết kế test case Boundary Value. | Open |

---

## 🟢 What's Good
- Cấu trúc tài liệu bám sát MBFS Golden Template.
- Việc áp dụng các chuẩn CMR_03, CMR_04, CF_01... rất rõ ràng, đảm bảo tính nhất quán trên hệ thống.
- Yêu cầu validate cho các trường số đặc thù được định nghĩa rõ ràng.

## 🧪 Testability Outlook
**What CAN be tested now:**
- Toàn bộ luồng CRUD báo cáo (Thêm, sửa, xóa nháp).
- Giao diện, phân trang, bộ lọc thời hạn, kiểm tra quyền truy cập theo CMR_03.
- Tính năng tự động tính tổng (auto-sum), tự động tăng STT, thêm xóa hàng CMR_15.
- Validate Number fields (>0, >=0).

**What CANNOT be tested yet:**
- Việc nộp báo cáo "trống" (Không phát sinh nghiệp vụ) bị block do mâu thuẫn rule số dòng tối thiểu.
- Validate dữ liệu cột "Hình thức ĐT" bảng 2 (đang là Textbox tự do).

## 📌 Summary & Recommendation
Tài liệu cung cấp khối lượng thông tin tốt, quy trình chuẩn chỉnh, đủ điều kiện để team QA bắt đầu viết Test Cases cho các luồng Positive (Happy Path) và cơ chế Validate số/giao diện chung. Tuy nhiên, một số vấn đề về mâu thuẫn loại Field, và định nghĩa "Bảng rỗng" cần được BA làm rõ để hoàn tất thiết kế Test Case Negative và Test theo giá trị rỗng.
**Khuyến nghị:** `CONDITIONALLY READY`. Vui lòng rà soát và phản hồi 5 câu hỏi trong Backlog.
