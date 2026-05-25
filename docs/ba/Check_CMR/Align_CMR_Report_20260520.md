# ALIGN CMR — REPORT

**Tiêu đề:** Kế hoạch cập nhật CMR — Phân hệ Báo cáo | Đã cập nhật theo BA confirm & Phân tích ảnh hưởng chi tiết
**Ngày tạo:** 2026-05-20
**Tác giả:** Antigravity Agent
**Phiên bản:** v7.0 (Scan TOÀN BỘ folder SRS-report — 55 UC folders + CMR + Process, 230+ violations) — Cập nhật M2/M3 audited status 2026-05-21
**Ghi chú:** Bản plan này tương tự CMR_Implementation_Plan_Mobile_v5, chuyển đổi áp dụng cho Phân hệ Báo cáo (Report). Thêm bảng Impact Analysis chi tiết bao phủ toàn bộ thư mục SRS-report. Bổ sung rule số mới: **15 chữ số nguyên + 5 chữ số thập phân**. v6.0 bổ sung: Toast/Inline Validation violations từ `list-toast-messages.md`, Prefix mã báo cáo violations từ `appendices.md`.
**BA Confirm (2026-05-20):** Textbox max=255 ✅ | Numeric 15+5 ✅ | Báo cáo tài chính không cần adjust riêng ✅ | Số nguyên (không thập phân) max=15 ✅

---

## A. TRƯỜNG TEXT (Textbox / Textarea) — CMR_06

| ID  | Tiêu chí                                                | Rule đã xác nhận                                                                                                                                                      |         Trạng thái         | Ghi chú thay đổi                                                    |
| :-- | :-------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------: | :--------------------------------------------------------------------- |
| A01 | Tự động xóa khoảng trắng đầu/cuối                | Hệ thống tự động xóa khoảng trắng ở đầu và cuối giá trị người dùng nhập**khi out-click**. VD: `" Nguyễn Văn A "` → `"Nguyễn Văn A"`     |         ✅ Xác nhận         | ✅ Xác nhận                                                          |
| A02 | Người dùng chỉ nhập toàn khoảng trắng             | Sau khi xóa khoảng trắng thừa, nếu không còn ký tự nào → coi như chưa nhập gì → trường bắt buộc hiển thị lỗi `"Vui lòng nhập [tên trường]"` |         ✅ Xác nhận         |                                                                        |
| A03 | Áp dụng cho ô nhập mật khẩu (Password)              | Không áp dụng — Phân hệ Report không có trường Password                                                                                                         |              N/A              |                                                                        |
| A04 | Thông báo lỗi khi bỏ trống bắt buộc                | `"Vui lòng nhập [tên trường]"` — VD: `"Vui lòng nhập Số công văn"`                                                                                         |         ✅ Xác nhận         | ✅ Xác nhận                                                          |
| A05 | Placeholder text box / text area                          | `"Nhập [tên trường]"`                                                                                                                                               |         ✅ Xác nhận         |                                                                        |
| A06 | Độ dài tối đa mặc định                            | -**Textbox: 255 ký tự** `<br>`- **Textarea: 3000 ký tự** `<br>`- Các trường có rule riêng sẽ được quy định rõ trong SRS từng UC          | ✅**BA CONFIRMED: 255** | Max textbox = 255 ký tự (không phải 500). Textarea = 3000 ký tự. |
| A07 | Thông báo lỗi khi nhập quá số ký tự               | `"[Tên trường] không được vượt quá [maxlength] ký tự!"`                                                                                                     |         ✅ Xác nhận         | ✅ Xác nhận                                                          |
| A08 | Thông báo lỗi khi nhập chưa đủ ký tự tối thiểu | `"[Tên trường] nhập chưa đủ [minlength] ký tự!"`                                                                                                               |         ✅ Xác nhận         | ✅ Xác nhận                                                          |

### Phân tích ảnh hưởng (Impact Analysis) - Mục A

**⚠️ Nhóm vi phạm Textbox max (đang 500 → đổi 255)**

| UC                  | Trường bị ảnh hưởng              | Hiện trạng | Thay đổi cần thực hiện                                                                                                                                     |
| :------------------ | :------------------------------------- | :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **UC011-034** | Số công văn (Tab B.IV.2, field #25) | Max 500      | Sửa maxlength →**255 ký tự**. Error: `"Số công văn không được vượt quá 255 ký tự"`. Sửa required: `"Vui lòng nhập Số công văn"` |
| **UC035-040** | Tất cả textbox fields                | Max 500      | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                     |
| **UC041-046** | Tất cả textbox fields                | Max 500      | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                     |
| **UC047-052** | Tất cả textbox fields                | Max 500      | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                     |
| **UC053-058** | Tất cả textbox fields                | Max 500      | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                     |
| **UC059-064** | Tất cả textbox fields                | Max 500      | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                     |
| **UC065-070** | Row 4 (textbox)                        | Max 500      | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                     |
| **UC071-088** | Số công văn (Tab B.IV.2)            | Max 500      | Sửa maxlength →**255 ký tự**. Error: `"Số công văn không được vượt quá 255 ký tự"`. Sửa required: `"Vui lòng nhập Số công văn"` |

**⚠️ UC089-184 vi phạm Textbox max (50 / 100 / 200 / 250 → 255) — BỔ SUNG MỚI**

| UC                  | Trường bị ảnh hưởng                                                                                                                            | Hiện trạng                    | Thay đổi cần thực hiện                                                                                                                                         |
| :------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **UC089-094** | C2 Mã số dự án / Số GCNĐT (text tự do)                                                                                                        | Max 50                          | Sửa maxlength →**255 ký tự**. Error: `"Mã số dự án không được vượt quá 255 ký tự"`                                                         |
| **UC089-094** | C4 Tên dự án/DN, C11 Thời hạn, C12 Địa chỉ, C13 Tên NĐT NN, C14 Địa chỉ NĐT NN, C16 Tên NĐT VN, C17 Địa chỉ NĐT VN, C19 Ghi chú | Chưa khai báo max             | Khai báo maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                    |
| **UC095-100** | C2 Mã số dự án, C9 Ghi chú                                                                                                                      | C2=Max 50; C9=Max 500           | Sửa maxlength →**255 ký tự** cho cả hai. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                             |
| **UC101-106** | Field 4 Mã số dự án, Field 6 Tên dự án/DN                                                                                                     | Field 4=Max 50; Field 6=Max 250 | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                         |
| **UC101-106** | Field 8 Số QD/Công văn                                                                                                                            | Max 50                          | ⚠️**Cần BA confirm**: Code field → giữ max 50. Text tự do → sửa max 255<br />**BA CONFIRM:** Code field -> giữ max 50; Text tự do -> max 255 |
| **UC107-112** | Các textbox trong bảng nhập liệu                                                                                                                 | Không khai báo max (trống)   | Khai báo maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                    |
| **UC113-118** | Các textbox thuộc bảng nhập liệu                                                                                                                | Max 50                          | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                         |
| **UC119-124** | Các textbox thuộc bảng nhập liệu                                                                                                                | Max 50                          | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                         |
| **UC167-172** | Field 4 Mã số GCNĐKDTRNN, Field 6 Số VB xác nhận ĐKGDNH, Field 9 Số văn bản chấp thuận                                                   | Max 100 mỗi field              | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                         |
| **UC167-172** | Field 11 Cơ quan cấp, Field 14 Tên tổ chức tín dụng                                                                                           | Max 200 mỗi field              | Sửa maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`                                                         |
| **UC167-172** | Field 13 Số tài khoản vốn ĐTRNN                                                                                                                 | Max 50                          | Sửa maxlength →**255 ký tự**. Error: `"Số tài khoản vốn ĐTRNN không được vượt quá 255 ký tự"`                                             |
| **UC179-184** | Field 7 Số văn bản chấp thuận chấm dứt                                                                                                        | Max 100                         | Sửa maxlength →**255 ký tự**. Error: `"Số văn bản không được vượt quá 255 ký tự"`                                                           |

**⚠️ KCN/KKT UCs vi phạm Textbox max / không khai báo max**

| UC                  | Trường bị ảnh hưởng                 | Hiện trạng        | Thay đổi cần thực hiện                                                                                                   |
| :------------------ | :---------------------------------------- | :------------------ | :---------------------------------------------------------------------------------------------------------------------------- |
| **UC263-268** | Thời gian dự kiến hoàn thành         | Max 50              | Sửa maxlength →**255 ký tự**. Error: `"Thời gian dự kiến hoàn thành không được vượt quá 255 ký tự"` |
| **UC263-268** | Quy mô công nghệ (Công suất xử lý) | Chưa khai báo max | Khai báo maxlength →**255 ký tự**. Error: `"Quy mô công nghệ không được vượt quá 255 ký tự"`          |
| **UC311-316** | Fields 18, 19 (textbox)                   | Không có max      | Khai báo maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`              |
| **UC329-334** | Field 9 (textbox)                         | Không có max      | Khai báo maxlength →**255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`              |

**⚠️ Textarea max vi phạm (2000 → 3000)**

| UC                  | Trường bị ảnh hưởng                                                       | Hiện trạng | Thay đổi cần thực hiện                                                                                        |
| :------------------ | :------------------------------------------------------------------------------ | :----------- | :----------------------------------------------------------------------------------------------------------------- |
| **UC011-034** | Tình hình thực hiện triển khai (field #57), Mục tiêu dự án (field #69) | Max 2000     | Sửa maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`      |
| **UC041-046** | C-001 (textarea)                                                                | Max 2000     | Sửa maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`      |
| **UC047-052** | Sections 68, 69 (textarea)                                                      | Max 2000     | Sửa maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`      |
| **UC053-058** | Tất cả textarea fields                                                        | Max 2000     | Sửa maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`      |
| **UC173-178** | Field 17 Lý do kéo dài                                                       | Max 2000     | Sửa maxlength →**3000 ký tự**. Error: `"Lý do kéo dài không được vượt quá 3000 ký tự"`     |
| **UC179-184** | Field 13 Lý do chấm dứt                                                      | Max 2000     | Sửa maxlength →**3000 ký tự**. Error: `"Lý do chấm dứt không được vượt quá 3000 ký tự"`    |
| **UC185-190** | Lý do / giải pháp (Row 14)                                                   | Max 2000     | Sửa maxlength →**3000 ký tự**. Error: `"Lý do / giải pháp không được vượt quá 3000 ký tự"` |

**⚠️ Textarea max vi phạm (1000 → 3000) — BỔ SUNG MỚI**

| UC                  | Trường bị ảnh hưởng                                          | Hiện trạng                                   | Thay đổi cần thực hiện                                                                                                          |
| :------------------ | :----------------------------------------------------------------- | :--------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| **UC089-094** | C10 Mục tiêu, C18 Ưu đãi đầu tư                            | Chưa khai báo max (CMR_06 default cũ = 500) | Khai báo maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`                   |
| **UC095-100** | C7 Nội dung điều chỉnh trước, C8 Nội dung điều chỉnh sau | Bộ đếm ký tự = 1000, chưa khai báo rõ  | Sửa maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`                        |
| **UC101-106** | Field 10 Ghi chú (Textarea)                                       | Max 500                                        | Sửa maxlength →**3000 ký tự**. Error: `"Ghi chú không được vượt quá 3000 ký tự"`                               |
| **UC161-166** | Textarea Lý do / Mô tả (nhiều field)                           | Default = 500 cũ                              | Khai báo maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`                   |
| **UC167-172** | Field 12 Địa chỉ trụ sở tại nước ngoài                    | Max 500                                        | Sửa maxlength →**3000 ký tự**. Error: `"Địa chỉ trụ sở tại nước ngoài không được vượt quá 3000 ký tự"` |
| **UC179-184** | Textarea Lý do/Mô tả (các field khác)                         | Default = 500 cũ                              | Khai báo maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`                   |
| **UC191-196** | Row 20 (textarea)                                                  | Max 1000                                       | Sửa maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`                        |
| **UC209-214** | Row 103 (textarea)                                                 | Max 1000                                       | Sửa maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`                        |
| **UC215-220** | Row 40 (textarea)                                                  | Max 1000                                       | Sửa maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`                        |
| **UC245-250** | Fields 12, 13, 14 (textarea)                                       | Max 1000                                       | Sửa maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`                        |
| **UC263-268** | Tất cả textarea fields                                           | Max 1000                                       | Sửa maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"`                        |

**⚠️ Textarea max vi phạm (< 1000)**

| UC                  | Trường bị ảnh hưởng | Hiện trạng | Thay đổi cần thực hiện                                                                                                     |
| :------------------ | :------------------------ | :----------- | :------------------------------------------------------------------------------------------------------------------------------ |
| **UC367-372** | Lý do (textarea)         | Max 400      | ✅**BA confirmed**: Sửa maxlength → **3000 ký tự**. Error: `"Lý do không được vượt quá 3000 ký tự"` |

**⚠️ KCN/KKT UCs không khai báo max Textarea**

| UC                  | Trường bị ảnh hưởng                                                                    | Hiện trạng         | Thay đổi cần thực hiện                                                                                        |
| :------------------ | :------------------------------------------------------------------------------------------- | :------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **UC335-340** | Tất cả textarea fields                                                                     | Không khai báo max | Khai báo maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"` |
| **UC341-346** | Textarea fields (2.6.1, 2.6.2, II.1, 1.2.7, 2.1.7, 2.1.9, 2.1.10, 2.1.14–2.1.16, 3.6, 3.28) | Không khai báo max | Khai báo maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"` |
| **UC353-358** | Tất cả textarea fields                                                                     | Không khai báo max | Khai báo maxlength →**3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự"` |

**⚠️ Placeholder violations (12+ UCs) — BỔ SUNG MỚI**

| UC                  | Trường                                           | Hiện trạng                                               | Đúng theo chuẩn                                                       |
| :------------------ | :------------------------------------------------- | :--------------------------------------------------------- | :----------------------------------------------------------------------- |
| **UC011-034** | Search bar                                         | `"Nhập dữ liệu"`                                      | → Sửa:`"Tìm kiếm nhanh theo mã báo cáo"`                        |
| **UC053-058** | Field 92                                           | `"Nhập dữ liệu"`                                      | → Sửa:`"Nhập [tên trường cụ thể]"`                             |
| **UC089-094** | C4, C12, C13, C14, C16, C17, C19 (text fields)     | Không có placeholder                                     | → Thêm:`"Nhập [tên trường cụ thể]"` cho từng field            |
| **UC089-094** | C10 Mục tiêu, C18 Ưu đãi đầu tư (textarea) | Không có placeholder                                     | → Thêm:`"Nhập [tên trường cụ thể]"`                            |
| **UC095-100** | C7, C8 (Textarea nội dung điều chỉnh)          | Không có placeholder                                     | → Thêm:`"Nhập [tên trường cụ thể]"`                            |
| **UC113-118** | Placeholder trong bảng nhập liệu                | Dài > 30 ký tự                                          | → Rút gọn, tối đa ~30 ký tự theo chuẩn                           |
| **UC119-124** | Placeholder trong bảng nhập liệu                | Dài > 30 ký tự                                          | → Rút gọn, tối đa ~30 ký tự theo chuẩn                           |
| **UC143-148** | Placeholder trong bảng nhập liệu                | Dài 37 ký tự                                            | → Rút gọn placeholder                                                 |
| **UC149-154** | Placeholder trong bảng nhập liệu                | Dài 36 ký tự                                            | → Rút gọn placeholder                                                 |
| **UC173-178** | Field 17 Lý do kéo dài (textarea)               | Placeholder dài 54 ký tự                                | → Rút gọn:`"Nhập lý do kéo dài thời hạn chuyển lợi nhuận"` |
| **UC209-214** | Row 59                                             | `"Nhập dữ liệu"`                                      | → Sửa:`"Nhập [tên trường cụ thể]"`                             |
| **UC215-220** | Row 4                                              | `"Nhập dữ liệu"`                                      | → Sửa:`"Nhập [tên trường cụ thể]"`                             |
| **UC311-316** | Rows 131-132                                       | `"Nhập Trong nước"`, `"Nhập Nước ngoài"`        | → Sửa:`"Nhập [tên trường cụ thể]"`                             |
| **UC329-334** | Row 9                                              | `"Nhập Văn bản thu hồi chủ trương ĐT/GCNĐKĐT"` | → Rút gọn placeholder                                                 |
| **UC335-340** | Row 125                                            | `"Nhập giá trị"`                                      | → Sửa:`"Nhập [tên trường cụ thể]"`                             |
| **UC341-346** | Row 190                                            | `"Nhập Lợi ích khác"`                                | → Kiểm tra lại cho đúng chuẩn                                      |
| **UC347-352** | Rows 125-130                                       | `"Nhập giá trị từ 20-100%"`                          | → Sửa:`"Nhập [tên trường cụ thể]"`                             |

**⚠️ Required error violations (8+ UCs) — BỔ SUNG MỚI**

| UC                             | Text hiện tại                                                        | Đúng theo chuẩn                                                              |
| :----------------------------- | :--------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| **UC065-070**            | `"Vui lòng nhập [tên trường]"` (có dấu `.`)                 | → Sửa:`"Vui lòng nhập [tên trường]"`                                   |
| **UC089-094**            | Chưa khai báo required error cho C4, C10, C12...                     | → Bổ sung:`"Vui lòng nhập [tên trường]"` cho tất cả field bắt buộc |
| **UC095-100**            | Required message C7, C8 chưa rõ                                      | → Bổ sung:`"Vui lòng nhập [tên trường]"`                               |
| **UC161-166**            | Required message các field text/textarea chưa đầy đủ             | → Bổ sung đầy đủ:`"Vui lòng nhập [tên trường]"`                    |
| **UC167-172**            | Required message fields 4, 6, 9, 11, 14 chưa rõ                      | → Đảm bảo:`"Vui lòng nhập [tên trường]"`                             |
| **UC185-190**            | `"Trường bắt buộc."`                                             | → Sửa:`"Vui lòng nhập [tên trường]"`                                   |
| **UC191-196**            | `"Trường bắt buộc."`                                             | → Sửa:`"Vui lòng chọn [tên trường]"`                                   |
| **UC245-250**            | Row 83: có dấu `.` ở cuối                                        | → Sửa:`"Vui lòng nhập [tên trường]"`                                   |
| **UC367-372**            | Row 263:`"Vui lòng nhập Lý do"`                                   | → Sửa:`"Vui lòng nhập Lý do"`                                            |
| **UC364-366, UC367-372** | Empty state `"Không có dữ liệu."`                                | → Sửa:`"Không có dữ liệu"`                                              |
| **UC367-372**            | `"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."` | → Bỏ `.` ở cuối cùng                                                     |

---

## B. TRƯỜNG MÃ (Code Field) — CMR mới cho Report

| ID  | Tiêu chí                                                                   | Rule đã xác nhận                                                                                                    | Trạng thái | Ghi chú thay đổi           |
| :-- | :--------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :-----------: | :---------------------------- |
| B01 | Tự động xóa khoảng trắng đầu/cuối                                   | Hệ thống tự động xóa khoảng trắng ở đầu và cuối**khi out-click**. VD: `" ABC123 "` → `"ABC123"` | ✅ Xác nhận |                               |
| B02 | Người dùng chỉ nhập toàn khoảng trắng                                | Sau khi xóa, nếu rỗng → coi như chưa nhập → lỗi `"Vui lòng nhập [tên trường]"`                          | ✅ Xác nhận |                               |
| B03 | Placeholder                                                                  | `"Nhập [tên trường]"`                                                                                             | ✅ Xác nhận |                               |
| B04 | Độ dài tối đa mặc định                                               | **50 ký tự**                                                                                                    | ✅ Xác nhận | ✅ Xác nhận                 |
| B05 | Thông báo lỗi khi nhập khoảng trắng ở giữa và tiếng Việt có dấu | `"Mã không bao gồm khoảng trắng và ký tự có dấu"`                                                           | ✅ Xác nhận | ⚠️ NEW RULE, bỏ dấu `.` |

### Phân tích ảnh hưởng (Impact Analysis) - Mục B

| UC                    | Trường bị ảnh hưởng | Hiện trạng                                 | Thay đổi cần thực hiện                                                                                                                                                                           |
| :-------------------- | :------------------------ | :------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **UC185-190**   | Mã dự án               | Max length chưa khai báo rõ               | Khai báo max =**50 ký tự**. Áp dụng rule B05: `"Mã không bao gồm khoảng trắng và ký tự có dấu"`. Thêm dấu `!` vào cuối error message                                     |
| **UC191-196**   | Mã số thuế             | Max 10/13 số. Error chưa chuẩn            | Áp dụng rule B05:`"Mã không bao gồm khoảng trắng và ký tự có dấu"`. Sửa error format có dấu `!`                                                                                    |
| **UC203-208**   | Mã thông báo           | Max length chưa khai báo                   | Khai báo max =**50 ký tự**. Áp dụng rule B05. Thêm dấu `!` vào cuối error message                                                                                                    |
| **UC239-298**   | Mã KCN / Mã dự án     | Max length không đồng nhất               | Chuẩn hóa max =**50 ký tự**. Áp dụng rule B05: `"Mã không bao gồm khoảng trắng và ký tự có dấu"`                                                                              |
| **Tất cả UC** | Trường mã báo cáo    | CMR_09 ghi pattern nhưng error chưa chuẩn | Khi nhập khoảng trắng hoặc tiếng Việt có dấu vào trường mã → hiển thị lỗi:`"Mã không bao gồm khoảng trắng và ký tự có dấu"`. Error message không có dấu `.` ở cuối |

---

## C. TRƯỜNG SỐ (Numeric) — CMR_05 (Đã cập nhật rule số mới)

| ID   | Tiêu chí                                                      | Rule đã xác nhận                                                                                                                                                                                                                                          |       Trạng thái       | Ghi chú thay đổi                                                                                                                       |
| :--- | :-------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| C01  | Placeholder                                                     | `"Nhập [tên trường]"`                                                                                                                                                                                                                                   |      ✅ Xác nhận      |                                                                                                                                           |
| C02  | Ký tự hợp lệ                                                | Chấp nhận: chữ số,`-`, `.` (thập phân), `,` (phân cách hàng nghìn). Block ký tự không hợp lệ                                                                                                                                             |      ✅ Xác nhận      |                                                                                                                                           |
| C03  | Trường >= 0                                                   | Không chấp nhận dấu `-` ở đầu                                                                                                                                                                                                                        |      ✅ Xác nhận      |                                                                                                                                           |
| C04  | Không cắt thập phân                                         | Giữ nguyên giá trị người dùng nhập                                                                                                                                                                                                                    |      ✅ Xác nhận      |                                                                                                                                           |
| C05  | Max length mặc định                                          | **21 ký tự** (15 nguyên + 1 `.` + 5 thập phân)                                                                                                                                                                                                   | ✅**BA CONFIRMED** | Áp dụng 15+5 cho toàn bộ trường số.                                                                                                |
| C05b | **RULE MỚI — Cấu trúc phần nguyên và thập phân** | **Phần nguyên: tối đa 15 chữ số**. **Phần thập phân: tối đa 5 chữ số**. Hệ thống cho phép nhập: `111,234,567,899,999.12345`. Nếu phần nguyên > 15 → báo lỗi. Nếu phần thập phân > 5 → block không cho nhập thêm. | ✅**BA CONFIRMED** | Áp dụng cho**toàn bộ** trường số. Không cần adjust riêng cho báo cáo tài chính.                                       |
| C06  | Error — Bắt buộc                                             | `"Vui lòng nhập [tên trường]"`                                                                                                                                                                                                                         |      ✅ Xác nhận      | ✅ Xác nhận                                                                                                                             |
| C07  | Error — Vượt giới hạn số (Numeric)                        | `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`                                                                                                                                                  | ⚠️**CẬP NHẬT** | Thay thế message cũ `"nhập quá ký tự cho phép"`. Hiển thị khi vượt phần nguyên hoặc khi nhập quá 5 chữ số thập phân |

### Phân tích ảnh hưởng (Impact Analysis) - Mục C

**⚠️ 5 UCs vi phạm Numeric max (đang 20 → đổi 21 tổng / 15 nguyên + 5 thập phân)**

| UC                  | Trường bị ảnh hưởng | Hiện trạng | Thay đổi cần thực hiện                                                                                                                                                                                           |
| :------------------ | :------------------------ | :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **UC041-046** | Row 202 (numeric field)   | Max 20       | Sửa: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` |
| **UC047-052** | Row 276 (numeric field)   | Max 20       | Sửa: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` |
| **UC053-058** | Row 271 (numeric field)   | Max 20       | Sửa: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` |
| **UC059-064** | Row 242 (numeric field)   | Max 20       | Sửa: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` |
| **UC065-070** | Row 251 (numeric field)   | Max 20       | Sửa: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` |

**⚠️ KCN/KKT UCs vi phạm Numeric max digit precision**

| UC                  | Trường bị ảnh hưởng | Hiện trạng                                                                                        | Thay đổi cần thực hiện                                                                                                                                                                                                  |
| :------------------ | :------------------------ | :-------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **UC251-256** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC257-262** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC263-268** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC269-274** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC275-280** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC281-286** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC287-292** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC293-298** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC299-304** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC305-310** | Fields 12-15, 20-23       | **⚠️ VI PHẠM NGHIÊM TRỌNG**: đang ghi "tối đa **2** chữ số phần thập phân" | Sửa ngay →**5 chữ số thập phân**. Đây là trường hợp DUY NHẤT ghi sai số thập phân. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` |
| **UC311-316** | Tất cả trường số     | Chỉ ghi ">=0", không khai báo digit precision                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC317-322** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC323-328** | Tất cả trường số     | Chỉ ghi ">=0", không khai báo digit precision                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC329-334** | Tất cả trường số     | Chỉ ghi ">=0", không khai báo digit precision                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC335-340** | Tất cả trường số     | Có range nhưng không khai báo digit precision                                                   | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC341-346** | Tất cả trường số     | Có range nhưng không khai báo digit precision                                                   | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC347-352** | Tất cả trường số     | Có range nhưng không khai báo digit precision                                                   | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |
| **UC353-358** | Tất cả trường số     | Không khai báo digit precision                                                                    | Bổ sung: phần nguyên →**15 chữ số**, phần thập phân → block sau **5 chữ số**. Error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`    |

**⚠️ Tất cả UCs có trường số — cần verify maxlength**

| UC Group                                  | Số lượng UC | Ảnh hưởng                                                                       |
| :---------------------------------------- | :------------- | :--------------------------------------------------------------------------------- |
| **UC011-034** (Báo cáo gộp)      | 1              | Kinh phí (Tab B.IV.3 cột 12-14), Vốn đăng ký (Tab A.IV.4) — cần verify max |
| **UC035-040, UC041-046, UC047-052** | 3              | Diện tích, số lượng — cần verify max                                        |
| **UC053-058, UC059-064, UC065-070** | 3              | Các trường số tài chính — cần verify max                                   |
| **UC071-088**                       | 1              | Các trường số — cần verify max                                               |
| **UC185-190, UC191-196, UC197-202** | 3              | Tiền tệ, lợi nhuận — áp dụng 15+5                                           |
| **UC239-298** (KCN/KKT)             | 6              | Diện tích, quy mô vốn — áp dụng 15+5                                        |
| **UC299-372**                       | 4              | Các trường số — áp dụng 15+5                                                |

**⚠️ Error message violations (numeric fields)**

| UC                    | Text hiện tại                                                | Đúng theo chuẩn                                           |
| :-------------------- | :------------------------------------------------------------- | :----------------------------------------------------------- |
| **Tất cả UC** | `"Ký tự không hợp lệ, chỉ chấp nhận..."` (có `.`) | → Bỏ `.` ở cuối                                        |
| **UC065-070**   | `"Giá trị phải lớn hơn 0."`                             | →`"Giá trị phải lớn hơn 0"`                          |
| **UC065-070**   | `"Không tìm thấy dữ liệu năm trước."`                | →`"Không tìm thấy dữ liệu năm trước"` (bỏ `.`) |
| **UC065-070**   | `"Dữ liệu trùng NĐT+Dự án."`                           | →`"Dữ liệu trùng NĐT+Dự án"` (bỏ `.`)            |

---

## D. DROPDOWN / COMBOBOX — CMR_07

| ID  | Tiêu chí                                              | Rule đã xác nhận                                                                                               | Trạng thái | Ghi chú thay đổi |
| :-- | :------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------- | :-----------: | :------------------ |
| D01 | Placeholder mặc định trong form                      | `"Chọn [tên trường]"`                                                                                        | ✅ Xác nhận |                     |
| D02 | Giá trị mặc định trong filter dropdown             | `"Tất cả"`                                                                                                     | ✅ Xác nhận |                     |
| D03 | Error — Bắt buộc chưa chọn                         | `"Vui lòng chọn [tên trường]"`                                                                              | ✅ Xác nhận | ✅ Xác nhận       |
| D04 | Không tìm thấy kết quả                             | Hiển thị text `"Không tìm thấy kết quả"` trong list dropdown                                              | ✅ Xác nhận | Bỏ dấu `.`      |
| D05 | Highlight option đã chọn khi mở lại                | ✅ Đúng                                                                                                          | ✅ Xác nhận |                     |
| D06 | Tên quá dài                                          | Cắt ngắn +`"... "`                                                                                             | ✅ Xác nhận |                     |
| D07 | Searchable Dropdown — Hiển thị Placeholder khi clear | Khi xóa hết keyword → dropdown hiển thị lại**placeholder**                                             | ✅ Xác nhận | ⚠️ NEW RULE       |
| D08 | Searchable Dropdown — Tap ra ngoài khi đang clear    | Nếu clear (trống) mà tap ra ngoài → chọn lại**"Tất cả"** (với filter) hoặc rỗng (với form bắt buộc) | ✅ Xác nhận | ⚠️ NEW RULE       |

### Phân tích ảnh hưởng (Impact Analysis) - Mục D

| UC                                        | Trường bị ảnh hưởng              | Hiện trạng                                                       | Thay đổi cần thực hiện                                                                                          |
| :---------------------------------------- | :------------------------------------- | :----------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| **UC185-190**                       | Dự án (Dropdown)                     | Error:`"Trường bắt buộc"`                                    | → Sửa thành:`"Vui lòng chọn Dự án"` — không có dấu `.`                                                |
| **UC191-196, UC197-202**            | Các dropdown filter                   | Error:`"Trường bắt buộc"`                                    | → Sửa thành:`"Vui lòng chọn [tên trường]"` — không có dấu `.`                                        |
| **UC011-034**                       | Năm báo cáo (Yearpicker)            | Error required:`"Vui lòng nhập Năm báo cáo"` (thiếu `!`) | → Sửa thành:`"Vui lòng chọn Năm báo cáo"`                                                                  |
| **UC011-034**                       | Tên dự án, Tên NĐT (Dropdown API) | Error required thiếu `!`                                        | → Thêm dấu `!` vào cuối error message: `"Vui lòng chọn Tên dự án"` và `"Vui lòng chọn Tên NĐT"` |
| **UC035-040, UC041-046, UC047-052** | Filter: Năm, Kỳ báo cáo            | Chưa có rule D07 + D08 mô tả clear keyword                     | Bổ sung mô tả rule D07 + D08 vào SRS                                                                             |
| **Tất cả UC** (Danh sách)        | Filter dropdown — Empty state         | `"Không tìm thấy kết quả."` có dấu `.`                  | → Bỏ dấu `.` thành: `"Không tìm thấy kết quả"` — không có `.` ở cuối                             |
| **Tất cả UC**                     | Filter dropdown — "Tất cả"          | CMR_16 đã có, verify áp dụng                                  | Đảm bảo CMR_16 được áp dụng đồng nhất                                                                     |

---

## E. Ô TÌM KIẾM (Search Box) — CMR_06

| ID  | Tiêu chí                                           | Rule đã xác nhận                                             | Trạng thái | Ghi chú thay đổi |
| :-- | :--------------------------------------------------- | :--------------------------------------------------------------- | :-----------: | :------------------ |
| E01 | Placeholder                                          | `"Tìm kiếm nhanh theo [điều kiện]"`                       | ✅ Xác nhận |                     |
| E02 | Tìm kiếm tự động (không cần Enter)            | ✅ Đúng                                                        | ✅ Xác nhận |                     |
| E03 | Loại tìm kiếm                                     | Gần đúng — không cần nhập đúng toàn bộ từ khóa      | ✅ Xác nhận |                     |
| E04 | Tự động xóa khoảng trắng đầu/cuối từ khóa | Tự xóa khoảng trắng thừa trước khi thực hiện tìm kiếm | ✅ Xác nhận |                     |
| E05 | Max length                                           | **255 ký tự**                                            | ✅ Xác nhận | ✅ Xác nhận       |
| E06 | Xóa hết từ khóa                                  | Danh sách về trạng thái mặc định (filter Tất cả)        | ✅ Xác nhận |                     |

### Phân tích ảnh hưởng (Impact Analysis) - Mục E

**⚠️ 6 UCs vi phạm Search max (200 → 255)**

| UC                  | Hiện trạng | Thay đổi cần thực hiện                                                                                      |
| :------------------ | :----------- | :--------------------------------------------------------------------------------------------------------------- |
| **UC035-040** | Max 200      | Sửa maxlength →**255 ký tự**. Error: `"Từ khóa tìm kiếm không được vượt quá 255 ký tự"` |
| **UC041-046** | Max 200      | Sửa maxlength →**255 ký tự**. Error: `"Từ khóa tìm kiếm không được vượt quá 255 ký tự"` |
| **UC047-052** | Max 200      | Sửa maxlength →**255 ký tự**. Error: `"Từ khóa tìm kiếm không được vượt quá 255 ký tự"` |
| **UC053-058** | Max 200      | Sửa maxlength →**255 ký tự**. Error: `"Từ khóa tìm kiếm không được vượt quá 255 ký tự"` |
| **UC059-064** | Max 200      | Sửa maxlength →**255 ký tự**. Error: `"Từ khóa tìm kiếm không được vượt quá 255 ký tự"` |
| **UC065-070** | Max 200      | Sửa maxlength →**255 ký tự**. Error: `"Từ khóa tìm kiếm không được vượt quá 255 ký tự"` |

**⚠️ KCN/KKT UCs vi phạm Search max / không khai báo**

| UC                  | Hiện trạng                | Thay đổi cần thực hiện                                                                                           |
| :------------------ | :-------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| **UC364-366** | Không khai báo max length | Khai báo maxlength →**255 ký tự**. Error: `"Từ khóa tìm kiếm không được vượt quá 255 ký tự"` |
| **UC367-372** | Không khai báo max length | Khai báo maxlength →**255 ký tự**. Error: `"Từ khóa tìm kiếm không được vượt quá 255 ký tự"` |

**⚠️ Placeholder violations (Search)**

| UC                                                   | Hiện trạng                               | Đúng theo chuẩn                                                               |
| :--------------------------------------------------- | :----------------------------------------- | :------------------------------------------------------------------------------- |
| **UC011-034**                                  | `"Nhập dữ liệu"`                      | → Sửa placeholder thành:`"Tìm kiếm nhanh theo mã báo cáo"`             |
| **UC035-040, UC041-046, UC047-052, UC053-058** | Placeholder có `...` hoặc chưa chuẩn | Chuẩn hóa placeholder theo rule E01:`"Tìm kiếm nhanh theo [điều kiện]"` |
| **UC239-298** (KCN/KKT series)                 | `"Tìm kiếm nhanh theo mã báo cáo"`  | ✅ Đúng chuẩn E01, không cần sửa                                           |

---

## F. LABEL

| ID  | Tiêu chí          | Rule đã xác nhận          | Trạng thái | Ghi chú |
| :-- | :------------------ | :---------------------------- | :-----------: | :------- |
| F01 | Trường bắt buộc | Đánh dấu `*` cạnh label | ✅ Xác nhận |          |

### Phân tích ảnh hưởng (Impact Analysis) - Mục F

| UC Bị Ảnh Hưởng     | Hiện Trạng Data                                             | Hành Động Cập Nhật Cần Thiết                                               |
| :---------------------- | :------------------------------------------------------------ | :-------------------------------------------------------------------------------- |
| **Tất cả form** | Đã hiển thị dấu `*` nhưng cần đảm bảo nhất quán | Map chuẩn trong UI Wireframe. Verify tất cả trường Required đều có `*`. |

---

## G. TỔNG HỢP MAX LENGTH (đã cập nhật)

| ID  | Loại trường                                                       |       Max Length       |              Trạng thái              |
| :-- | :------------------------------------------------------------------- | :--------------------: | :-------------------------------------: |
| G01 | Textbox                                                              | **255 ký tự** |      ✅**BA CONFIRMED: 255**      |
| G02 | Textarea                                                             | **3000 ký tự** |              ✅ Xác nhận              |
| G03 | Trường Mã (Code)                                                  |  **50 ký tự**  |              ✅ Xác nhận              |
| G04 | Trường Số (Numeric) — Phần nguyên                              |  **15 ký tự**  |  ✅**BA CONFIRMED: 15 nguyên**  |
| G05 | Trường Số (Numeric) — Phần thập phân                          |  **5 ký tự**  | ✅**BA CONFIRMED: 5 thập phân** |
| G06 | Trường Số (Numeric) — Tổng cộng (nguyên +`.` + thập phân) |  **21 ký tự**  |   ✅**BA CONFIRMED: 21 tổng**   |
| G07 | Search Box                                                           | **255 ký tự** |              ✅ Xác nhận              |

### Phân tích ảnh hưởng (Impact Analysis) - Mục G

| UC Bị Ảnh Hưởng                  | Hiện Trạng Data                                    | Hành Động Cập Nhật Cần Thiết                                                                                                |
| :----------------------------------- | :--------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| **Tất cả UC** (Trường số) | Max length không đồng nhất hoặc chưa khai báo | Áp dụng chuẩn:**15 nguyên + 5 thập phân = 21 ký tự tổng**. Số nguyên (không thập phân) = **15 ký tự**. |
| **UC065-070**                  | Row 4 textbox                                        | Verify max = 255, không phải 500                                                                                                 |

---

## H. TỔNG HỢP ERROR MESSAGE (đã cập nhật)

| ID  | Loại lỗi                                                   | Message chuẩn                                                                                               |       Trạng thái       |
| :-- | :----------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- | :----------------------: |
| H01 | Bắt buộc — Text / Numeric                                 | `"Vui lòng nhập [tên trường]"`                                                                        |      ✅ Xác nhận      |
| H02 | Bắt buộc — Dropdown                                       | `"Vui lòng chọn [tên trường]"`                                                                        |      ✅ Xác nhận      |
| H03 | Vượt max length (Text)                                     | `"[Tên trường] không được vượt quá [maxlength] ký tự!"`                                        |      ✅ Xác nhận      |
| H04 | Chưa đủ min length (Text)                                 | `"[Tên trường] nhập chưa đủ [minlength] ký tự!"`                                                  |      ✅ Xác nhận      |
| H05 | Vượt max length (Numeric)                                  | `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` | ⚠️**CẬP NHẬT** |
| H06 | Trường Mã — Khoảng trắng giữa / tiếng Việt có dấu | `"Mã không bao gồm khoảng trắng và ký tự có dấu"`                                                |      ✅ Xác nhận      |
| H07 | Số công văn — Thiếu `/`                               | `"Số công văn chưa đúng chuẩn, thiếu dấu "/""`                                                    |      ✅ Xác nhận      |
| H08 | Số công văn — Thiếu `-`                               | `"Số công văn chưa đúng chuẩn, thiếu dấu "-""`                                                    |      ✅ Xác nhận      |
| H09 | Số công văn — Sai format                                 | `"Vui lòng nhập lại thông tin"`                                                                        |      ✅ Xác nhận      |
| H10 | Lỗi hệ thống / mạng / Timeout                            | Toast T05:`"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."`                             |      ✅ Xác nhận      |
| H11 | Empty State — Không có dữ liệu                          | `"Không có dữ liệu"` (không có dấu `.` ở cuối)                                                  |      ✅ Xác nhận      |
| H12 | Empty State — Không tìm thấy kết quả tìm kiếm        | `"Không tìm thấy kết quả phù hợp"` (không có dấu `.`)                                          |      ✅ Xác nhận      |

> **Lưu ý:** Toàn bộ error message không có dấu `.` ở cuối câu.

### Phân tích ảnh hưởng (Impact Analysis) - Mục H

**⚠️ Violations theo nhóm — 200+ violations phát hiện**

| Nhóm                                      | UC                                                                                | Số lỗi | Mô tả                                                              |
| :----------------------------------------- | :-------------------------------------------------------------------------------- | :------: | :------------------------------------------------------------------- |
| **Trường bắt buộc sai format**   | UC185-190, UC191-196                                                              |    2    | Dùng `"Trường bắt buộc."` thay vì `"Vui lòng nhập..."`   |
| **Trường bắt buộc thiếu `!`** | 35+ UCs (UC011-088: 8 UCs, UC089-184: 16 UCs, UC185-250: 6 UCs, UC251-372: 5 UCs) |   50+   | `"Vui lòng nhập [tên trường]"` nhưng có dấu `.` ở cuối |
| **Error message có `.` ở cuối** | 15+ UCs                                                                           |   20+   | Bỏ `.`, thêm `!` where appropriate                             |
| **Empty state có `.`**            | 20+ UCs                                                                           |   25+   | `"Không có dữ liệu."` → `"Không có dữ liệu"`            |

---

## I. BUTTON — CF_common_functions

| ID  | Button                            | Điều kiện Disabled                                                                                   | Điều kiện Enabled                                       | Trạng thái | Ghi chú                                                                                            |
| :-- | :-------------------------------- | :------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------- | :-----------: | :-------------------------------------------------------------------------------------------------- |
| I01 | Submit / Lưu / Gửi              | — (Không disable kể cả khi form chưa hợp lệ)                                                     | Luôn enabled                                              | ✅ Xác nhận | Các button đều sẽ luôn enabled, validate khi tap                                               |
| I02 | Submit — Khi gọi API            | Đang load API                                                                                          | Sau khi API trả về                                       | ✅ Xác nhận | Tránh double-click                                                                                 |
| I03 | Submit — Double-tap              | Xử lý bằng loading state                                                                             | —                                                         | ✅ Xác nhận |                                                                                                     |
| I04 | Nút Xác nhận (Dialog)          | —                                                                                                      | Luôn enabled                                              | ✅ Xác nhận |                                                                                                     |
| I05 | Nút Hủy (Dialog)                | —                                                                                                      | Luôn enabled                                              | ✅ Xác nhận |                                                                                                     |
| I06 | Nút Áp dụng (Filter)           | —                                                                                                      | Luôn enabled                                              | ✅ Xác nhận | Kể cả khi validate filter sai                                                                     |
| I07 | Nút Đặt lại (Filter)          | —                                                                                                      | Luôn enabled                                              | ✅ Xác nhận |                                                                                                     |
| I08 | Nút Thử lại (Error)            | Khi đang load API                                                                                      | Sau timeout / lỗi                                         | ✅ Xác nhận |                                                                                                     |
| I09 | Nút [Xem trước] — PDF Preview | **Disabled** khi báo cáo chưa được Lưu nháp lần nào (bản ghi chưa tồn tại trong DB) | **Enabled** sau khi đã Lưu nháp ít nhất 1 lần | ✅ Xác nhận | Tham chiếu CF_01, CF_03. Không disable khi form chưa valid — chỉ disable khi chưa Lưu nháp. |
| I10 | Nút [Hủy] — Dirty Form Guard   | CMR_14: Hiển thị popup cảnh báo khi form dirty                                                      | —                                                         | ✅ Xác nhận |                                                                                                     |

### Phân tích ảnh hưởng (Impact Analysis) - Mục I

| UC                                        | Button bị ảnh hưởng     | Hiện trạng trong SRS                                           | Thay đổi cần thực hiện                                                                |
| :---------------------------------------- | :-------------------------- | :--------------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| **UC011-034** (Báo cáo gộp)      | Nút [Lưu nháp]           | Cần verify: đang disabled khi form chưa valid?                | Sửa →**Luôn Enabled**. Tap → validate → hiện lỗi inline.                      |
| **UC011-034**                       | Nút [Nộp báo cáo]       | Cần verify: disabled khi form chưa hợp lệ?                   | Sửa →**Luôn Enabled**. Tap → validate toàn bộ N tabs.                          |
| **UC185-190, UC191-196, UC197-202** | Nút [Nộp báo cáo]       | Cần verify: disabled khi form chưa hợp lệ?                   | Sửa →**Luôn Enabled**.                                                            |
| **UC035-040, UC041-046, UC047-052** | Nút [Áp dụng] (Filter)   | Cần verify: disabled khi có validation error?                  | Sửa →**Luôn Enabled**.                                                            |
| **UC065-070, UC071-088**            | Nút [Lưu] / [Nộp]        | Chưa có mô tả “Luôn Enabled” trong SRS                    | Bổ sung:**Luôn Enabled** theo I01.                                                 |
| **UC089-094 → UC184**              | Tất cả nút Submit / Lưu | **C⚠️ TOÀN BỘ thiếu ký `Luôn Enabled`** trong SRS | Bổ sung mô tả `Luôn Enabled` cho tất cả button trong nhóm này.                   |
| **Tất cả UC có API**             | Nút Call API               | Chưa mô tả loading state rõ ràng                            | Bổ sung: Tap →**loading state (spinner)** → sau khi API trả về mới enable lại |
| **UC011-034**                       | Nút [Xem trước]          | Disabled khi chưa Lưu nháp (đúng rule I09)                  | Giữ nguyên theo I09                                                                      |

---

## I-bis. EXPORT / PREVIEW — CMR UPDATE ⚠️ BỔ SUNG MỚI (2026-05-22)

> **Nguyên tắc:** Bỏ nút Export khỏi popup Preview. Preview chỉ hỗ trợ **In (Web Print)**. Nút Export được chuyển ra ngoài **Màn hình danh sách**.

| ID    | Tiêu chí                                                        | Rule đã xác nhận                                                                                                                                                                                                                  | Trạng thái  | Ghi chú                                                                                       |
| :---- | :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-----------: | :--------------------------------------------------------------------------------------------- |
| Ibis1 | Popup Preview — Chỉ có nút [In]                               | Khi mở popup Xem trước (PDF Preview), popup **chỉ hiển thị nút [In]** (Web Print). **Không có nút [Xuất báo cáo]** trong popup Preview.                                                                                   | ✅ Xác nhận | Lý do: Preview hiển thị cục data đang edit in-memory, không liên quan bản ghi trong DB.     |
| Ibis2 | Nút [Xuất báo cáo] — Chỉ ở Màn hình danh sách              | Nút [Xuất báo cáo] chỉ hiển thị tại **Màn hình danh sách** (cột Hành động). Tham chiếu: CF_04.                                                                                                                              | ✅ Xác nhận | Export lấy bản ghi đã lưu từ DB để xuất file.                                               |
| Ibis3 | Popup cảnh báo khi Export — Bản ghi chưa cập nhật mới nhất | Khi nhấn [Xuất báo cáo] từ Màn hình danh sách, nếu bản ghi có thay đổi chưa Lưu → hiển thị popup: **"Nội dung xuất file là bản đã lưu gần nhất. Vui lòng Lưu nháp trước khi xuất nếu muốn cập nhật."** | ✅ Xác nhận | Popup chỉ thông báo, user vẫn có thể chọn xuất bản cũ hoặc quay lại Lưu nháp trước.       |

### Phân tích ảnh hưởng (Impact Analysis) - Mục I-bis

| UC                                                                    | Vị trí bị ảnh hưởng                                                  | Hiện trạng                                                                                                  | Thay đổi cần thực hiện                                                                                                                                                |
| :-------------------------------------------------------------------- | :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **UC011-034** (Báo cáo gộp)                                  | Mô tả nút per-tab [Xem trước]; Bảng button Tab 1-4; Mục 3 xử lý | Popup Preview có nút [Xuất báo cáo] + [In]                                                                | Bỏ `[Xuất báo cáo]` khỏi popup Preview. Chỉ giữ `[In]`. Export chỉ từ Danh sách (row #8 Action Mapping).                                                          |
| **UC035-040, UC041-046, UC047-052**                           | Mô tả nút [Xem trước] trong form; Mục xử lý                       | Popup Preview có nút [Xuất báo cáo] + [In]                                                                | Bỏ `[Xuất báo cáo]` khỏi popup Preview. Chỉ giữ `[In]`.                                                                                                             |
| **UC053-058, UC059-064, UC065-070, UC071-088**                | Mô tả nút [Xem trước] trong form; Mục xử lý                       | Popup Preview có nút [Xuất báo cáo] + [In]                                                                | Bỏ `[Xuất báo cáo]` khỏi popup Preview. Chỉ giữ `[In]`.                                                                                                             |
| **UC239-298** (KCN/KKT)                                       | Mô tả nút [Xem trước] trong form (nếu có)                          | Cần verify — có thể có nút Export trong Preview                                                            | Bỏ `[Xuất báo cáo]` khỏi popup Preview nếu có. Chỉ giữ `[In]`.                                                                                                      |
| **Tất cả UC có nút Export trên Danh sách**                  | Cột Hành động — nút [Xuất báo cáo]                                 | Xuất trực tiếp, không có popup cảnh báo                                                                   | Bổ sung logic: Nếu bản ghi có thay đổi chưa Lưu → hiển thị popup cảnh báo Ibis3 trước khi xuất.                                                                   |
| **CF_04 (Common Function — Xuất báo cáo)**                    | Mô tả scope CF_04                                                      | CF_04 áp dụng cả từ Preview popup và Danh sách                                                            | Thu hẹp scope: CF_04 **chỉ áp dụng từ Màn hình danh sách**. Bỏ mô tả "Xuất báo cáo file đang xem từ Preview popup".                                              |

---

## K. TAB NAVIGATION — CMR_18 ⚠️ BỔ SUNG MỚI

> **CMR_18** quy định chuẩn điều hướng bàn phím (Tab key) trong các form nhập liệu.

| ID  | Tiêu chí                              | Rule đã xác nhận                                                                   | Trạng thái | Ghi chú |
| :-- | :-------------------------------------- | :------------------------------------------------------------------------------------- | :-----------: | :------- |
| K01 | Tab key điều hướng giữa các field | Nhấn Tab → focus chuyển đến field tiếp theo theo thứ tự logic                  | ✅ Xác nhận | CMR_18   |
| K02 | Tab ở field cuối cùng                | Nhấn Tab ở field cuối → focus quay về field đầu tiên (hoặc đến nút Submit) | ✅ Xác nhận |          |
| K03 | Shift+Tab                               | Di chuyển ngược                                                                     | ✅ Xác nhận |          |

### Phân tích ảnh hưởng (Impact Analysis) - Mục K

**⚠️ 13+ UCs chưa có tham chiếu CMR_18 trong SRS — BỔ SUNG MỚI**

| UC                  | Hiện trạng                              | Thay đổi cần thực hiện                                           |
| :------------------ | :---------------------------------------- | :-------------------------------------------------------------------- |
| **UC065-070** | Không có tham chiếu CMR_18 trong CF_01 | Bổ sung:`Tham chiếu CMR_18 Tab Navigation trên form nhập liệu` |
| **UC071-088** | Không có tham chiếu CMR_18             | Bổ sung tham chiếu CMR_18 vào CF_01                                |
| **UC107-112** | Không có tham chiếu CMR_18             | Bổ sung tham chiếu CMR_18                                           |
| **UC113-118** | Không có tham chiếu CMR_18             | Bổ sung tham chiếu CMR_18                                           |
| **UC119-124** | Không có tham chiếu CMR_18             | Bổ sung tham chiếu CMR_18                                           |
| **UC125-130** | Không có tham chiếu CMR_18             | Bổ sung tham chiếu CMR_18                                           |
| **UC131-136** | Không có tham chiếu CMR_18             | Bổ sung tham chiếu CMR_18                                           |
| **UC137-142** | Không có tham chiếu CMR_18             | Bổ sung tham chiếu CMR_18                                           |
| **UC143-148** | Không có tham chiếu CMR_18             | Bổ sung tham chiếu CMR_18                                           |
| **UC149-154** | Không có tham chiếu CMR_18             | Bổ sung tham chiếu CMR_18                                           |
| **UC299-304** | Không có tham chiếu CMR_18             | Bổ sung tham chiếu CMR_18                                           |

---

## J. SỐ CÔNG VĂN ( CMR_13 — Đã có trong Report)

CMR_13 đã được định nghĩa đầy đủ trong CMR_common_business_rules. Không cần thay đổi rule nghiệp vụ. Chỉ cần cập nhật error message:

| ID  | Tiêu chí                     | Rule hiện tại                                           | Thay đổi cần thực hiện                      |
| :-- | :----------------------------- | :-------------------------------------------------------- | :----------------------------------------------- |
| J01 | Error — Thiếu `/`          | `"Số công văn chưa đúng chuẩn, thiếu dấu "/""` | ✅ Đã chuẩn, verify không có `.` ở cuối |
| J02 | Error — Thiếu `-`          | `"Số công văn chưa đúng chuẩn, thiếu dấu "-""` | ✅ Đã chuẩn, verify không có `.` ở cuối |
| J03 | Error — Sai format tổng thể | `"Vui lòng nhập lại thông tin"`                     | ✅ Đã chuẩn                                   |

---

## K. TOAST & INLINE VALIDATION MESSAGES — Violations từ `list-toast-messages.md`

> **Nguồn:** `docs/BA/SRS-report/CMR/list-toast-messages.md` (v1.5, cập nhật 2026-05-19)

### K1. Inline Validation Messages — Vi phạm dấu `.` ở cuối

| Mã           | Nội dung hiện tại                                                                                 | Đúng theo chuẩn H (bỏ `.`)                                                                              | UC áp dụng                 |
| :------------ | :--------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :--------------------------- |
| **V01** | `"Trường bắt buộc"`                                                                            | → Sửa thành:`"Vui lòng nhập [tên trường]"` hoặc `"Vui lòng chọn [tên trường]"` theo H01/H02 | Tất cả UC                  |
| **V04** | `"Sai định dạng số."` (có `.`)                                                              | →`"Sai định dạng số"` (bỏ `.`)                                                                      | Tất cả UC có trường số |
| **V08** | `"Kinh phí quyết toán không được vượt kinh phí thực hiện."` (có `.`)                | →`"Kinh phí quyết toán không được vượt kinh phí thực hiện"` (bỏ `.`)                        | UC011-034                    |
| **V09** | `"Tổng kinh phí quyết toán không được vượt kinh phí thực hiện."` (có `.`)          | →`"Tổng kinh phí quyết toán không được vượt kinh phí thực hiện"` (bỏ `.`)                  | UC011-034                    |
| **V10** | `"Đã tồn tại báo cáo cho năm này."` (có `.`)                                            | →`"Đã tồn tại báo cáo cho năm này"` (bỏ `.`)                                                    | UC011-034                    |
| **V11** | `"Vui lòng nhập tình hình thực hiện triển khai."` (có `.`)                               | →`"Vui lòng nhập tình hình thực hiện triển khai"` (bỏ `.`)                                       | UC011-034                    |
| **V12** | `"Giá trị phải lớn hơn 0."` (có `.`)                                                       | →`"Giá trị phải lớn hơn 0"` (bỏ `.`)                                                               | UC011-034                    |
| **V13** | `"Nhà đầu tư này đã được ghi nhận quan tâm đến dự án này."` (có `.`)           | →`"Nhà đầu tư này đã được ghi nhận quan tâm đến dự án này"` (bỏ `.`)                   | UC011-034                    |
| **V14** | `"Năm báo cáo không hợp lệ."` (có `.`)                                                    | →`"Năm báo cáo không hợp lệ"` (bỏ `.`)                                                            | UC011-034                    |
| **V15** | `"Diện tích đất không được vượt tổng diện tích quỹ đất của dự án."` (có `.`) | →`"Diện tích đất không được vượt tổng diện tích quỹ đất của dự án"` (bỏ `.`)         | UC011-034                    |

### K2. Toast Messages — Vi phạm dấu `.` ở cuối

| Mã           | Nội dung hiện tại                                                                             | Đúng theo chuẩn                                                                                | Ghi chú                                                                           |
| :------------ | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------- |
| **T05** | `"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."`                           | → Giữ nguyên (H10 cho phép `.` giữa câu, nhưng bỏ `.` cuối cùng)                    | ⚠️ Cần BA confirm: Toast T05 có giữ `.` cuối hay bỏ?<br />BA CONFIRM: bỏ |
| **T06** | `"Báo cáo cho [Phạm vi báo cáo] đã chọn đã được lập bởi [Tên người lập]"`   | ✅ Không có `.` cuối — OK                                                                   |                                                                                    |
| **T17** | `"Kỳ báo cáo đã tồn tại trong hệ thống. Vui lòng kiểm tra lại."` (có `.` cuối) | →`"Kỳ báo cáo đã tồn tại trong hệ thống. Vui lòng kiểm tra lại"` (bỏ `.` cuối) | UC041-046                                                                          |

### K3. Alert Messages — Vi phạm dấu `.` ở cuối

| Mã           | Nội dung hiện tại                                                                                                      | Đúng theo chuẩn                                                                                                         |
| :------------ | :------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------- |
| **A01** | `"Dữ liệu không khớp với [Phạm vi báo cáo] đã chọn. Vui lòng kiểm tra lại."` (có `.` cuối)            | →`"Dữ liệu không khớp với [Phạm vi báo cáo] đã chọn. Vui lòng kiểm tra lại"` (bỏ `.` cuối)            |
| **A02** | `"Cấu trúc file không đúng định dạng template. Vui lòng sử dụng file template đã tải."` (có `.` cuối) | →`"Cấu trúc file không đúng định dạng template. Vui lòng sử dụng file template đã tải"` (bỏ `.` cuối) |
| **A03** | `"Định dạng file không được hỗ trợ. Vui lòng sử dụng file template đã tải."` (có `.` cuối)           | →`"Định dạng file không được hỗ trợ. Vui lòng sử dụng file template đã tải"` (bỏ `.` cuối)           |
| **A04** | `"Không thể đọc file. Vui lòng kiểm tra lại file và thử lại."` (có `.` cuối)                              | →`"Không thể đọc file. Vui lòng kiểm tra lại file và thử lại"` (bỏ `.` cuối)                              |

### K4. Popup Messages — Vi phạm dấu `.` ở cuối

| Mã           | Nội dung hiện tại                                                                                                                        | Đúng theo chuẩn                                                                                                                           |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------- |
| **P01** | `"Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác."` (có `.` cuối)      | →`"Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác"` (bỏ `.` cuối)      |
| **P03** | `"Báo cáo [Tên báo cáo] đã được lập bởi [Tên nhà đầu tư]. Vui lòng không lập lại báo cáo này."` (có `.` cuối) | →`"Báo cáo [Tên báo cáo] đã được lập bởi [Tên nhà đầu tư]. Vui lòng không lập lại báo cáo này"` (bỏ `.` cuối) |

### K5. V01 — Xung đột với CMR chuẩn

| Vấn đề                      | Chi tiết                                                                                                                                                                                                                                                                                                          |
| :----------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **V01 hiện tại**       | `"Trường bắt buộc"` — dùng chung cho tất cả trường khi Lưu nháp/Nộp                                                                                                                                                                                                                                 |
| **CMR chuẩn (H01/H02)** | `"Vui lòng nhập [tên trường]"` / `"Vui lòng chọn [tên trường]"`                                                                                                                                                                                                                                      |
| **Xung đột**           | `list-toast-messages.md` V01 ghi `"Trường bắt buộc"` nhưng CMR_05/06/07 yêu cầu `"Vui lòng nhập/chọn [tên trường]"`                                                                                                                                                                             |
| **Hành động**         | ⚠️**Cần BA confirm**: V01 áp dụng cho trường hợp nào? Nếu chỉ dùng khi Lưu nháp (validate tối thiểu) thì giữ `"Trường bắt buộc"`. Nếu dùng khi Nộp → phải đổi thành `"Vui lòng nhập/chọn [tên trường]"` theo CMR chuẩn.<br />BA CONFIRM: đồng bộ theo CMR chuẩn |

---

## L. PREFIX MÃ BÁO CÁO — Violations từ `appendices.md`

> **Nguồn:** `docs/BA/SRS-report/CMR/appendices.md` (v2.0, cập nhật 2026-05-11)

### L1. Prefix sai — DTNN_ → FDI_

| Vấn đề              | Chi tiết                                                                                      |
| :--------------------- | :--------------------------------------------------------------------------------------------- |
| **Rule chuẩn**  | Prefix mã báo cáo phải dùng `FDI_` cho phân hệ Đầu tư nước ngoài vào Việt Nam |
| **Hiện trạng** | Nhiều file SRS đang dùng prefix `DTNN_` (sai)                                             |
| **Hành động** | Cập nhật toàn bộ file SRS dùng `DTNN_` → `FDI_`                                      |

### L2. UCs bị ảnh hưởng bởi prefix sai

| UC                            | Prefix hiện tại   | Prefix đúng        | Ghi chú                        |
| :---------------------------- | :------------------ | :------------------- | :------------------------------ |
| **UC035-040**           | `DTNN_AIII3_[ID]` | →`FDI_AIII3_[ID]` | Mẫu A.III.3                    |
| **UC041-046**           | `DTNN_AIII1_[ID]` | →`FDI_AIII1_[ID]` | Mẫu A.III.1                    |
| **UC047-052**           | `DTNN_AIII2_[ID]` | →`FDI_AIII2_[ID]` | Mẫu A.III.2                    |
| **UC053-058**           | `DTNN_AIII4_[ID]` | →`FDI_AIII4_[ID]` | Mẫu A.III.4                    |
| **UC059-064**           | `DTNN_AIII5_[ID]` | →`FDI_AIII5_[ID]` | Mẫu A.III.5                    |
| **UC065-070**           | `DTNN_AIV1_[ID]`  | →`FDI_AIV1_[ID]`  | Mẫu A.IV.1                     |
| **UC089-094**           | `FDI_AIV5_[ID]`   | ✅ Đúng            | Đã dùng đúng prefix        |
| **UC185-220** (ĐTRNN)  | `ODI_` prefix     | ✅ Đúng            | Phân hệ ĐTRNN dùng `ODI_` |
| **UC239-358** (KCN/KKT) | `EZ_` prefix      | ✅ Đúng            | Phân hệ KCN/KKT dùng `EZ_` |

### L3. Danh sách prefix chuẩn (tham chiếu)

| Phân hệ      | Prefix    | Mô tả                                | UCs áp dụng          |
| :------------- | :-------- | :------------------------------------- | :--------------------- |
| **FDI**  | `FDI_`  | Đầu tư nước ngoài vào Việt Nam | UC011-184              |
| **ODI**  | `ODI_`  | Đầu tư ra nước ngoài             | UC185-220              |
| **EZ**   | `EZ_`   | Quản lý KCN, KKT                     | UC239-358              |
| **PROM** | `PROM_` | Xúc tiến đầu tư                   | UC011-034 (Tab B.IV.x) |

---

## M. DANH MỤC TÀI LIỆU THAM CHIẾU TRONG FOLDER SRS-REPORT

### M1. Cấu trúc folder (52 UC folders + 3 thư mục hỗ trợ)

| Thư mục                      | Nội dung                                                                                                                                                       | Số files        |
| :----------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
| `CMR/`                       | Common rules: CMR_common_business_rules, CF_common_functions, CS_common_screen_logic, CS_template, appendices, list-toast-messages, PENDING_assumptions_backlog | 7 files          |
| `Process/`                   | Quy trình nghiệp vụ: CMCĐT_BCTK_01 → 09, Mục lục                                                                                                         | 10 files (.docx) |
| `design/`                    | (Trống)                                                                                                                                                        | 0 files          |
| `UC-ID/`                     | Mapping UC-ID → folder (55 entries, bao gồm UC221-226, UC227-231, UC233-238 mới + UC367-369 và UC370-372 tách riêng)                                      | 55 subfolders    |
| `UC011-034` → `UC367-372` | SRS source files + audited files + question-backlogs + wireframe images                                                                                         | 55 UC folders    |

### M2. UCs có file audited (đã review)

| UC        | File audited                                                                  | Phiên bản mới nhất |
| :-------- | :---------------------------------------------------------------------------- | :--------------------- |
| UC011-034 | `UC011-034_bo-ho-so-xuc-tien-dau-tu_audited_20260514_v1.md`                 | v1                     |
| UC035-040 | `UC035-040_bao-cao-truoc-khi-thuc-hien-du-an-dt_audited_20260515_v2.md`     | v2                     |
| UC041-046 | `UC041-046_bao-cao-tinh-hinh-thuc-hien-du-an-dt-quy_audited_20260515_v2.md` | v2                     |
| UC047-052 | `UC047-052_thuc-hien-du-an-dau-tu-nam_audited_20260515_v3.md`               | v3                     |
| UC053-058 | `UC053-058_dau-khi-du-an-dau-tu_audited_20260516_v2.md`                     | v2                     |
| UC059-064 | `UC059-064_dau-khi-dau-tu-nam_audited_20260518_v2.md`                       | v2                     |
| UC065-070 | `UC065-070_tong-hop-dtnn-dia-ban_audited_20260514_v1.md`                    | v1                     |
| UC071-088 | `UC071-088_bo-ho-so-bao-cao-dtnn-dia-ban_audited_20260514_v1.md`            | v1                     |
| UC089-094 | `UC089-094_CapMoiGCNDKDT_audited_v8.md`                                     | v8                     |
| UC095-100 | `UC095-100_DieuChinhGCNDKDT_audited_v4.md`                                  | v4                     |
| UC101-106 | `UC101-106_TamNgungChamDutDTNN_audited_v5.md`                               | v5                     |
| UC107-112 | `UC107-112_BaoCaoTongHopXuatNhapKhau_audited_v3.md`                         | v3                     |
| UC113-118 | `UC113-118_XuatKhauDTNN_audited_v4.md`                                      | v4                     |
| UC119-124 | `UC119-124_NhapKhauDTNN_audited_v4.md`                                      | v4                     |
| UC125-130 | `UC125-130_TaiChinhDiaBanDTNN_audited_v4.md`                                | v4                     |
| UC131-136 | `UC131-136_TaiChinhDoanhnghiepDTNN_audited_v4.md`                           | v4                     |
| UC137-142 | `UC137-142_LaoDongNuocNgoaiQuocTich_audited_v3.md`                          | v3                     |
| UC143-148 | `UC143-148_LaoDongNuocNgoaiDiaBan_audited_v3.md`                            | v3                     |
| UC149-154 | `UC149-154_ChuyenGiaoCongNgheDiaBan_audited_v4.md`                          | v4                     |
| UC185-190 | `UC185-190_BaoCaoNamDTRNN_audited_20260511_v1.md`                           | v1                     |
| UC191-196 | `UC191-196_BaoCaoNamTaiChinhDTRNN_audited_20260511_v1.md`                   | v1                     |
| UC197-202 | `UC197-202_audited_v1.md`                                                   | v1                     |
| UC203-208 | `UC203-208_QLNNBoDTRNN_audited_20260511_v1.md`                              | v1                     |
| UC209-214 | `UC209-214_DKGDNHChamDutDTRNN_audited_20260511_v1.md`                       | v1                     |
| UC215-220 | `UC215-220_ChuyenVonDTRNN_audited_v1.md`                                    | v1                     |
| UC221-226 | `UC221-226_audited-v1.md`                                                   | v1                     |
| UC227-231 | `UC227-231_thuc-hien-du-an-dt-nam_audited_20260521_v1.md`                   | v1                     |
| UC233-238 | `UC233-238_BaoCaoTruocKhiThucHienDuAnDT_audited-v1.md`                      | v1                     |
| UC299-304 | `UC299-304_bieu-tong-hop-kkt_audited_20260508_v4.md`                        | v4                     |
| UC305-310 | `UC305-310_BieuKhuPhiThueQuan_audited_20260508_v3.md`                       | v3                     |
| UC311-316 | `UC311-316_BaoCaoKCNKKT_audited_20260508_v2.md`                             | v2                     |
| UC317-322 | `UC317-322_DauTuTheoDoiTacKCN_audited_20260508_v2.md`                       | v2                     |
| UC323-328 | `UC323-328_DieuChinhDuAnKCN_audited_20260508_v2.md`                         | v2                     |
| UC329-334 | `UC329-334_bieu-thu-hoi-du-an-kcn_audited_20260521_v2.md`                   | v2                     |
| UC335-340 | `UC335-340_ChiSoDanhGiaHieuQuaKCNST_audited_20260514_v1.md`                 | v1                     |
| UC341-346 | `UC341-346_bieu-tong-hop-kcn-sinh-thai_audited_20260508_v4.md`              | v4                     |
| UC347-352 | `UC347-352_ChiSoDanhGiaDNSinhThai_audited_20260514_v2.md`                   | v2                     |
| UC353-358 | `UC353-358_GiamSatDNSinhThai_audited_20260508_v2.md`                        | v2                     |

### M3. UCs CHƯA có file audited (chỉ có SRS source)

| UC        | File SRS source                           | Ghi chú    |
| :-------- | :---------------------------------------- | :---------- |
| UC155-160 | `UC155-160_GiaoDatChoThuedat.md`        | Chưa audit |
| UC161-166 | `UC161-166_BaoCao6ThangDTRNN.md`        | Chưa audit |
| UC167-172 | `UC167-172_ThongBaoDTRNN.md`            | Chưa audit |
| UC173-178 | `UC173-178_KeoThoiHanChuyenLoiNhuan.md` | Chưa audit |
| UC179-184 | `UC179-184_ChamDutHoatDongDTRNN.md`     | Chưa audit |
| UC239-244 | `UC239-244_ThuHutDauTuKCN.md`           | Chưa audit |
| UC245-250 | `UC245-250_ThanhLapDieuChinhKCN.md`     | Chưa audit |
| UC251-256 | `UC251-256_ThucHienDuAnHaTangKCN.md`    | Chưa audit |
| UC257-262 | `UC257-262_SXKDTaiKCN.md`               | Chưa audit |
| UC263-268 | `UC263-268_NhaMayXLNTKCN.md`            | Chưa audit |
| UC269-274 | `UC269-274_LaoDongKCN.md`               | Chưa audit |
| UC275-280 | `UC275-280_DanhMucKCNQuyHoach.md`       | Chưa audit |
| UC281-286 | `UC281-286_SoLuongDienTichKKT.md`       | Chưa audit |
| UC287-292 | `UC287-292_ThuHutDauTuKKT.md`           | Chưa audit |
| UC293-298 | `UC293-298_QuyHoachDatKKT.md`           | Chưa audit |
| UC364-366 | `UC364-366_QuanLyBaoCaoDaNop.md`        | Chưa audit |
| UC367-372 | `UC367-372_QuanLyBaoCaoDaNhan.md`       | Chưa audit |

### M4. Process files (Quy trình nghiệp vụ)

| File                    | Mô tả                             |
| :---------------------- | :---------------------------------- |
| `CMCĐT_BCTK_01.docx` | Quy trình báo cáo thống kê #01 |
| `CMCĐT_BCTK_02.docx` | Quy trình báo cáo thống kê #02 |
| `CMCĐT_BCTK_03.docx` | Quy trình báo cáo thống kê #03 |
| `CMCĐT_BCTK_04.docx` | Quy trình báo cáo thống kê #04 |
| `CMCĐT_BCTK_05.docx` | Quy trình báo cáo thống kê #05 |
| `CMCĐT_BCTK_06.docx` | Quy trình báo cáo thống kê #06 |
| `CMCĐT_BCTK_07.docx` | Quy trình báo cáo thống kê #07 |
| `CMCĐT_BCTK_08.docx` | Quy trình báo cáo thống kê #08 |
| `CMCĐT_BCTK_09.docx` | Quy trình báo cáo thống kê #09 |
| `Mục lục.docx`      | Mục lục tổng hợp quy trình     |

---

## TỔNG HỢP VIOLATIONS — BẢNG ĐẾM (v6.0 — cập nhật sau scan toàn bộ)

| CMR Rule                                   | Số UCs bị ảnh hưởng |     Tổng số violations     | Mức độ                 |
| :----------------------------------------- | :----------------------: | :--------------------------: | :------------------------ |
| **A: Textbox max 255**               |         20+ UCs         |             25+             | Cao                       |
| **A: Textarea max 3000**             |         18+ UCs         |             20+             | Cao                       |
| **A: Placeholder chuẩn**            |         25+ UCs         |             30+             | TB                        |
| **B: Code field max 50**             |          4 UCs          |              4+              | TB                        |
| **C: Numeric max 15+5**              |         40+ UCs         |             50+             | **NGHIÊM TRỌNG**  |
| **C: Numeric sai spec (2 decimals)** |          2 UCs          |              2              | **NGHIÊM TRỌNG**  |
| **D: Dropdown error chuẩn**         |          6+ UCs          |              6+              | TB                        |
| **E: Search max 255**                |          8 UCs          |              8              | TB                        |
| **H: Empty state `.` → bỏ**      |         20+ UCs         |             25+             | TB                        |
| **H: Required error `!`**          |         35+ UCs         |             50+             | Cao                       |
| **H: Error message `.` → `!`**  |         15+ UCs         |             20+             | Cao                       |
| **I: Button enabled**                |          6 UCs          |              6+              | TB                        |
| **K: Inline Validation `.` cuối** |       Tất cả UC       |        10+ (V01-V15)        | Cao                       |
| **K: Toast/Alert/Popup `.` cuối** |       Tất cả UC       | 8+ (T05,T17,A01-A04,P01,P03) | TB                        |
| **K: V01 xung đột CMR**            |       Tất cả UC       |         1 (systemic)         | **CẦN BA CONFIRM** |
| **L: Prefix mã sai DTNN_ → FDI_**  |    6 UCs (UC035-070)    |              6              | TB                        |

---

## TỔNG HỢP VIOLATIONS (v6.0 — sau scan TOÀN BỘ folder SRS-report)

### Tổng quan số lượng

| Loại Violation                                      |                  Số UCs bị ảnh hưởng                  | Tổng số vi phạm | Mức độ                                                            |
| :--------------------------------------------------- | :--------------------------------------------------------: | :----------------: | :------------------------------------------------------------------- |
| **A: Textbox maxlength 255**                   |                          20+ UCs                          |        25+        | Cao                                                                  |
| **A: Textarea maxlength 3000**                 |                          18+ UCs                          |        20+        | Cao                                                                  |
| **A: Placeholder chuẩn**                      |                          25+ UCs                          |        30+        | Trung bình                                                          |
| **B: Code field max 50**                       |                           4 UCs                           |         4+         | Trung bình                                                          |
| **C: Numeric max 15+5 — CHƯA KHAI BÁO**     |                          40+ UCs                          |        50+        | **NGHIÊM TRỌNG**                                             |
| **C: Numeric SAI spec (sai số thập phân)**  | 4 UCs:**UC125-130, UC155-160, UC197-202, UC305-310** |         4         | **VI PHẠM NGHIÊM TRỌNG** — đang ghi 2 decimals thay vì 5 |
| **D: Dropdown error chuẩn**                   |                           6+ UCs                           |         6+         | Trung bình                                                          |
| **E: Search max 255**                          |                           8 UCs                           |         8         | Trung bình                                                          |
| **H: Empty state `.` → bỏ**                |                          20+ UCs                          |        25+        | Trung bình                                                          |
| **H: Required error `!` cuối**              |                          35+ UCs                          |        50+        | Cao                                                                  |
| **H: Error message `.` → `!`**            |                          15+ UCs                          |        20+        | Cao                                                                  |
| **I: Button enabled**                          |                           6 UCs                           |         6+         | Trung bình                                                          |
| **K: Inline Validation (V01-V15) `.` cuối** |                   Tất cả UC (systemic)                   |        10+        | Cao                                                                  |
| **K: Toast/Alert/Popup `.` cuối**           |                        Tất cả UC                        |         8+         | Trung bình                                                          |
| **K: V01 xung đột CMR chuẩn**               |                        Tất cả UC                        |    1 (systemic)    | **CẦN BA CONFIRM**                                            |
| **L: Prefix mã sai DTNN_ → FDI_**            |                     6 UCs (UC035-070)                     |         6         | Trung bình                                                          |

**TỔNG: 230+ violations across all UCs — Chỉ có UC239-244 (Biểu 2101) là gần fully compliant nhất**

---

## CHI TIẾT VIOLATIONS THEO NHÓM UC (v5.0)

### NHÓM 1: UC011-088 — 8 UCs chính

| UC                  |   Textbox   |   Textarea   |  Numeric  |   Search   |       Placeholder       |    Required    |                     Empty                     | Ghi chú                          |
| :------------------ | :---------: | :-----------: | :-------: | :---------: | :----------------------: | :-------------: | :--------------------------------------------: | :-------------------------------- |
| **UC011-034** | 500→255 ❌ | 2000→3000 ❌ | 20→21 ❌ | 200→255 ❌ | `"Nhập dữ liệu"` ❌ |   Cần verify   |       `"Chưa có báo cáo nào."` ❌       | Nhiều vi phạm nhất trong nhóm |
| **UC035-040** | 500→255 ❌ | 2000→3000 ❌ | 20→21 ❌ | 200→255 ❌ | `"Nhập dữ liệu"` ❌ |    Có `.`    |       `"Chưa có báo cáo nào."` ❌       | Email/SĐT error có `.`        |
| **UC041-046** | 500→255 ❌ | 2000→3000 ❌ | 20→21 ❌ | 200→255 ❌ |      Có `...` ❌      |    Có `.`    |       `"Chưa có báo cáo nào."` ❌       |                                   |
| **UC047-052** | 500→255 ❌ | 2000→3000 ❌ | 20→21 ❌ | 200→255 ❌ |      Có `...` ❌      |    Có `.`    | `"Kỳ báo cáo này chưa tới hạn..."` ❌ |                                   |
| **UC053-058** | 500→255 ❌ | 2000→3000 ❌ | 20→21 ❌ | 200→255 ❌ | `"Nhập dữ liệu"` ❌ |    Có `.`    |                  Cần verify                  | Cột 4+5: maxlength lẫn lộn     |
| **UC059-064** | 500→255 ❌ | 2000→3000 ❌ | 20→21 ❌ | 200→255 ❌ |            OK            |       OK       |                  Cần verify                  |                                   |
| **UC065-070** | 500→255 ❌ | 2000→3000 ❌ | 20→21 ❌ | 200→255 ❌ |            OK            | Thiếu `!` ❌ |                  Cần verify                  | Nhiều error message có `.`    |
| **UC071-088** | 500→255 ❌ | 2000→3000 ❌ | 20→21 ❌ | 200→255 ❌ |        Trống ❌        |    Có `.`    |                  Cần verify                  | Nhiều placeholder trống         |

### NHÓM 2: UC089-184 — 16 UCs

| UC                  |    Textbox    |    Textarea    |            Numeric            | Search |      Placeholder      |    Required    | Empty | Ghi chú                                             |
| :------------------ | :------------: | :-------------: | :----------------------------: | :----: | :--------------------: | :-------------: | :---: | :--------------------------------------------------- |
| **UC089-094** |   50→255 ❌   |       OK       |         Thiếu 15+5 ❌         |   OK   | `"Nhap muc tieu"` ❌ | Thiếu `!` ❌ |  OK  |                                                      |
| **UC095-100** |  500→255 ❌  |  1000→3000 ❌  |         Thiếu 15+5 ❌         |   OK   |       Trống ❌       | Thiếu `!` ❌ |  OK  |                                                      |
| **UC101-106** |   50→255 ❌   |  500→3000 ❌  |         Thiếu 15+5 ❌         |   OK   |       Trống ❌       | Thiếu `!` ❌ |  OK  |                                                      |
| **UC107-112** |   Trống ❌   |       OK       |         Thiếu 15+5 ❌         |   OK   |           OK           | Thiếu `!` ❌ |  OK  |                                                      |
| **UC113-118** |   50→255 ❌   |       OK       |         Thiếu 15+5 ❌         |   OK   |   Dài 37 ký tự ❌   | Thiếu `!` ❌ |  OK  |                                                      |
| **UC119-124** |   50→255 ❌   |       OK       |         Thiếu 15+5 ❌         |   OK   |   Dài 36 ký tự ❌   | Thiếu `!` ❌ |  OK  |                                                      |
| **UC125-130** |       OK       |       OK       | **Sai 2 decimals→5** ❌ |   OK   |           OK           | Thiếu `!` ❌ |  OK  | Diện tích: 2 decimals.**⚠️ BỔ SUNG MỚI** |
| **UC131-136** |       OK       |       OK       |         Thiếu 15+5 ❌         |   OK   |       Trống ❌       | Thiếu `!` ❌ |  OK  |                                                      |
| **UC137-142** |       OK       |       OK       |         Thiếu 15+5 ❌         |   OK   |           OK           | Thiếu `!` ❌ |  OK  |                                                      |
| **UC143-148** |       OK       |       OK       |         Thiếu 15+5 ❌         |   OK   |   Dài 37 ký tự ❌   | Thiếu `!` ❌ |  OK  |                                                      |
| **UC149-154** |       OK       |       OK       |         Thiếu 15+5 ❌         |   OK   |   Dài 36 ký tự ❌   | Thiếu `!` ❌ |  OK  |                                                      |
| **UC155-160** |       OK       |       OK       | **Sai 2 decimals→5** ❌ |   OK   |           OK           | Thiếu `!` ❌ |  OK  | Diện tích: 2 decimals.**⚠️ BỔ SUNG MỚI** |
| **UC161-166** |   20→255 ❌   | Trống→3000 ❌ |           20→21 ❌           |   OK   |       Trống ❌       | Thiếu `!` ❌ |  OK  | Fields 13-16: 20 ký tự                             |
| **UC167-172** | 50-200→255 ❌ |  500→3000 ❌  |         Thiếu 15+5 ❌         |   OK   |       Trống ❌       | Thiếu `!` ❌ |  OK  | Nhiều field 50-200 ký tự                          |
| **UC173-178** |       OK       | Trống→3000 ❌ |         Thiếu 15+5 ❌         |   OK   |   Dài 54 ký tự ❌   | Thiếu `!` ❌ |  OK  | Field 17 placeholder dài                            |
| **UC179-184** |  100→255 ❌  | Trống→3000 ❌ |         Thiếu 15+5 ❌         |   OK   |       Trống ❌       | Thiếu `!` ❌ |  OK  | Nhiều field 100 ký tự                             |

### NHÓM 3: UC185-250

| UC                  |                  Textbox                  |         Textarea         |               Numeric               | Search |           Placeholder           |                 Required                 |                 Empty                 | Ghi chú                         |
| :------------------ | :---------------------------------------: | :----------------------: | :---------------------------------: | :----: | :-----------------------------: | :--------------------------------------: | :-----------------------------------: | :------------------------------- |
| **UC185-190** |                 Trống ❌                 | 500→3000 ❌ (6 fields) |     Thiếu 15+5 ❌ (18+ fields)     |   OK   | `"Nhập tên..."` thường ❌ |      `"Trường bắt buộc."` ❌      | `"Không tìm thấy kết quả."` ❌ | Rất nhiều violations           |
| **UC191-196** |                100→255 ❌                | 1000→3000 ❌ (2 fields) |      Thiếu 15+5 ❌ (7 fields)      |   OK   | `"Nhập tên..."` thường ❌ |      `"Trường bắt buộc."` ❌      | `"Không tìm thấy kết quả."` ❌ | Tài khoản 100 ký tự          |
| **UC197-202** |          500→255 ❌ (3 fields)          | 500→3000 ❌ (8 fields) | **Sai 15+2 thay vì 15+5** ❌ |   OK   |               OK               |       Thiếu `!` ❌ (10 fields)       |                  OK                  | Numeric sai spec nghiêm trọng  |
| **UC203-208** |                50→255 ❌                |            OK            |           Thiếu 15+5 ❌           |   OK   |               OK               |                    OK                    |    `"Không có dữ liệu."` ❌    |                                  |
| **UC209-214** | 50→255 ❌ (2 fields) + 12 trong bảng ❌ |            OK            |     2 decimals→5 ❌ (2 fields)     |   OK   |               OK               |        Thiếu `!` ❌ (2 fields)        | `"Không tìm thấy kết quả."` ❌ | 12 textbox không có max        |
| **UC215-220** |        50-1000→255 ❌ (11 fields)        |            OK            |      12+2→15+5 ❌ (2 fields)      |   OK   |               OK               |        Thiếu `!` ❌ (1 field)        |                  OK                  | Nhiều field 1000 ký tự        |
| **UC239-244** |                    OK                    |            OK            |     Thiếu 15+5 ❌ (18+ fields)     |   OK   |               OK               |                    OK                    |                  OK                  | ✅**GẦN COMPLIANT NHẤT** |
| **UC245-250** |                    OK                    |      1000→3000 ❌      |      Thiếu 15+5 ❌ (7 fields)      |   OK   |               OK               | `"Vui lòng nhập..."` thiếu `!` ❌ |                  OK                  | Dropdown error `[Tên field]`  |

### NHÓM 4: UC251-372 (KCN/KKT)

| UC                  |   Textbox   |       Textarea       |                Numeric                |       Search       |             Placeholder             |             Required             |              Empty              | Ghi chú                              |
| :------------------ | :---------: | :------------------: | :------------------------------------: | :----------------: | :----------------------------------: | :------------------------------: | :------------------------------: | :------------------------------------ |
| **UC251-256** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                |                OK                |                                       |
| **UC257-262** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                |                OK                |                                       |
| **UC263-268** | 50→255 ❌ |    1000→3000 ❌    |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                |                OK                |                                       |
| **UC269-274** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                |                OK                |                                       |
| **UC275-280** | 100→255 ❌ |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                |                OK                |                                       |
| **UC281-286** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                |                OK                |                                       |
| **UC287-292** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |         Thiếu `!` ❌         |                OK                |                                       |
| **UC293-298** | 50→255 ❌ |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                |                OK                |                                       |
| **UC299-304** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                |                OK                |                                       |
| **UC305-310** |     OK     |          OK          | **Sai 2 decimals thay vì 5** ❌ |         OK         |                  OK                  |                OK                |                OK                | ⚠️**VI PHẠM NGHIÊM TRỌNG** |
| **UC311-316** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |     `"Nhập Trong nước"` ❌     |                OK                |                OK                |                                       |
| **UC317-322** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                | `"Không có dữ liệu..."` ❌ | Empty state có `.`                 |
| **UC323-328** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |      `"Vui lòng..."` ❌      |                OK                | Validation message                    |
| **UC329-334** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |     `"Nhập Văn bản..."` ❌     |         Thiếu `!` ❌         |                OK                |                                       |
| **UC335-340** |     OK     | OK (nhiều trường) |             Thiếu 15+5 ❌             |         OK         |       `"Nhập giá trị"` ❌       |                OK                |                OK                |                                       |
| **UC341-346** |     OK     |    OK (12 fields)    |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                |                OK                |                                       |
| **UC347-352** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         | `"Nhập giá trị từ 20-100%"` ❌ |                OK                |                OK                |                                       |
| **UC353-358** |     OK     |          OK          |             Thiếu 15+5 ❌             |         OK         |                  OK                  |                OK                |                OK                |                                       |
| **UC364-366** |     OK     |          OK          |                   OK                   | Chưa khai báo ❌ |                  OK                  |                OK                |                OK                |                                       |
| **UC367-372** |     OK     |     400→3000 ❌     |                   OK                   | Chưa khai báo ❌ |                  OK                  | `"Vui lòng nhập Lý do."` ❌ |      `"...phù hợp."` ❌      | Empty state có `.`                 |

---

## UCs ĐẠT COMPLIANT CAO NHẤT

| UC                  | Tên                          | Số Violations | Ghi chú                                                |
| :------------------ | :---------------------------- | :------------: | :------------------------------------------------------ |
| **UC239-244** | Biểu 2101 - Thu hút ĐT KCN |       1       | Numeric precision chưa khai báo — cần bổ sung 15+5 |
| UC251-256           | Biểu 2103                    |       1       | Numeric precision                                       |
| UC257-262           | Biểu 2104                    |       1       | Numeric precision                                       |
| UC269-274           | Biểu 2106 - Lao động KCN   |       1       | Numeric precision                                       |
| UC281-286           | Biểu 2108                    |       1       | Numeric precision                                       |
| UC299-304           | Biểu 2111                    |       1       | Numeric precision                                       |

---

## UCs CẦN CẬP NHẬT NHIỀU NHẤT

| UC                               | Số violations | Các lỗi chính                                                                          |
| :------------------------------- | :------------: | :---------------------------------------------------------------------------------------- |
| **UC185-190**              |      25+      | Textarea (6 fields), Numeric (18+ fields), Required (21 fields), Placeholder, Empty state |
| **UC011-034**              |      10+      | Textbox, Textarea, Numeric, Search, Placeholder, Error `.`                              |
| **UC035-040**              |       8+       | Textbox, Textarea, Numeric, Search, Placeholder, Error `.`                              |
| **UC197-202**              |      20+      | Textbox (3), Textarea (8), Numeric**SAI 15+2**, Required (10)                       |
| **UC089-094 → UC179-184** |  5-10 mỗi UC  | Textbox max, Numeric precision, Required thiếu `!`, Placeholder                        |

---

*Kết thúc v7.0 — Scan toàn bộ folder SRS-report hoàn tất (55 UC folders + CMR + Process). Tổng cộng **230+ violations** phát hiện trên **55 UCs**. **Không có UC nào hoàn toàn không có vi phạm** (trừ UC239-244 gần đạt chuẩn duy nhất). Bổ sung mới v6.0: Mục K (Toast/Inline Validation violations), Mục L (Prefix mã báo cáo), Mục M (Danh mục tài liệu tham chiếu đầy đủ). v7.0: Cập nhật M2/M3 audited status — 38 UCs đã có file audited, 17 UCs chưa audit (2026-05-21).*
